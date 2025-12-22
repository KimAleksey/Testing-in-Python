import pendulum

from typing import Any

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from utils_for_orchestration.utils_api import get_data_from_api
from utils_for_orchestration.utils_transform import transform_nested_fields
from utils_for_orchestration.utils_load_to_postgres import save_dict_to_postgres

# Конфигурация DAG
OWNER = "kim-av"
DAG_ID = "dag_for_loading_data_to_pg"
TAGS = ["example", "etl", "tests"]

# Длинное описание
LONG_DESCRIPTION = """
DAG for practice with testing in Python and DAGs.
"""

# Короткое описание
SHORT_DESCRIPTION = "Пример реализации DAG для ETL с использованием тестирования."

# Аргументы по-умолчанию
default_args = {
    "owner": OWNER,
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": pendulum.duration(minutes=3),
}


def extract(**context) -> dict[Any, Any]:
    """
    Функция, которая получает данные из API и пушит в xcom

    :param context: context выполнения таски
    :return: Dict - результат API
    """
    url = "https://randomuser.me/api/"
    result = get_data_from_api(url=url, time_out=600)
    return result


def transform(**context) -> dict[str, Any] | None:
    """
    Функция, которая забирает dict из xcom, сформированный ранее. И формирует новый xcom, который содержит
    dict с нужными полями и значениями для загрузки.

    :param context: context выполнения таски extract
    :return: Dict - строка для записи
    """
    ti = context.get("ti")
    api_data = ti.xcom_pull("extract")
    user_data = transform_nested_fields(api_data)
    return user_data


def load(**context) -> None:
    """
    Функция, которая забирает dict из xcom, сформированный ранее. Из этого значения формирует INSER query
    и выполняет его.

    :param context: context выполнения таски transform
    :return: None
    """
    ti = context.get("ti")
    user_row = ti.xcom_pull("transform")
    save_dict_to_postgres(conn_id="my_db", schema="ods", table="users", dict_row=user_row)


with DAG(
    dag_id=DAG_ID,
    description=SHORT_DESCRIPTION,
    schedule_interval="0 10 * * *",
    start_date=pendulum.datetime(2025, 12, 1),
    catchup=True,
    default_args=default_args,
    tags=TAGS,
    max_active_runs=1,
    max_active_tasks=1,
) as dag:

    start_task = EmptyOperator(
        task_id="start",
        dag=dag
    )

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    end_task = EmptyOperator(
        task_id="end",
        dag=dag
    )

    start_task >> extract_task >> transform_task >> load_task >> end_task