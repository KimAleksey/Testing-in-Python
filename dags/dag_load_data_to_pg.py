import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Конфигурация DAG
OWNER = "kim-av"
DAG_ID = "dag_for_loading_data_to_pg"
TAGS = ["example", "etl", "tests"]

LONG_DESCRIPTION = """
DAG for practice with testing in Python and DAGs.
"""

SHORT_DESCRIPTION = "Пример реализации DAG для ETL с использованием тестирования."

default_args = {
    "owner": OWNER,
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": pendulum.duration(minutes=3),
}

with DAG(
    dag_id=DAG_ID,
    description=SHORT_DESCRIPTION,
    schedule_interval='@daily',
    start_date=pendulum.datetime(2025, 12, 1),
    catchup=False,
    default_args=default_args,
    tags=TAGS,
    max_active_runs=1,
    max_active_tasks=1,
) as dag:

    start_task = EmptyOperator(
        task_id="start",
        dag=dag
    )


    end_taks = EmptyOperator(
        task_id="end",
        dag=dag
    )

    start_task >> end_taks