import pytest
from airflow.models import DagBag


class TestDagLoadDataToPg:
    DAG_ID = "dag_for_loading_data_to_pg"

    @pytest.fixture(scope="class")
    def dag_fixture(self):
        # Сканируем папку, загружаем все DAGs
        bag = DagBag(dag_folder="dags/etl", include_examples=False)
        # Ищем DAG с id dag_for_loading_data_to_pg
        dag = bag.dags.get(self.DAG_ID)
        # Проверяет, что DAG реально существует
        assert dag is not None, f"DAG {self.DAG_ID} doesn't exist"
        # Проверяем, что при импорте DAG-ов не было ошибок
        assert bag.import_errors == {}
        # Возвращаем DAG
        return dag

    def test_dag_loaded(self, dag_fixture):
        assert dag_fixture.dag_id == self.DAG_ID