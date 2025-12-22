import logging

from airflow.models.connection import Connection
from airflow.providers.postgres.hooks.postgres import PostgresHook

from handles.oltp.execute_custom_query import execute_custom_query

from dags.utils_for_orchestration.utils_load_to_postgres import save_dict_to_postgres
from dags.utils_for_orchestration.utils_api import get_data_from_api
from dags.utils_for_orchestration.utils_transform import transform_nested_fields

class TestSaveDictToPostgres:
    @staticmethod
    def create_pg_connection() -> Connection:
        return Connection(
            conn_type='postgres',
            host='localhost',
            port=5434,
            schema='demo',
            login='postgres',
            password='postgres',
        )

    @staticmethod
    def create_test_users() -> None:
        execute_custom_query(
            db_name = 'demo',
            host = 'localhost',
            user = 'postgres',
            password = 'postgres',
            port = 5434,
            query = """
                CREATE SCHEMA IF NOT EXISTS ods;
                
                DROP TABLE IF EXISTS ods.users;
                
                CREATE TABLE ods.users (
                    user_id bigserial NOT NULL,
                    created_at timestamptz DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    username text NULL,
                    "password" text NULL,
                    firstname text NULL,
                    lastname text NULL,
                    email text NULL,
                    country text NULL,
                    city text NULL,
                    CONSTRAINT users_pkey PRIMARY KEY (user_id)
                );
            """
        )

    def test_save_dict_to_postgres(self):
        conn = self.create_pg_connection()
        self.create_test_users()
        api_data = get_data_from_api(url="https://randomuser.me/api/", time_out=600)
        user_data = transform_nested_fields(api_data)
        save_dict_to_postgres(
            conn_id = conn,
            schema = 'ods',
            table = 'users',
            dict_row = user_data
        )
        pg_hook = PostgresHook(postgres_conn_id=None, connection=conn)

        rows = pg_hook.get_records(
            sql="select * from ods.users",
        )

        logging.info(*rows)

        assert len(rows) == 1