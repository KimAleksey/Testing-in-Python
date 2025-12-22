import pytest

from dags.utils_for_orchestration.utils_load_to_postgres import save_dict_to_postgres

class TestSaveDictToPostgres:
    @staticmethod
    def create_pg_connection():
