from handles.oltp.execute_custom_query import execute_custom_query
from handles.oltp.get_postgres_credentials import get_postgres_rec

if __name__ == "__main__":
    # Получаем путь до файла с реквизитами подключения к PG
    pg_credentials = get_postgres_rec()

    # Создаем схему
    execute_custom_query(
        db_name=pg_credentials["db_name"],
        port=pg_credentials["port"],
        host=pg_credentials["host"],
        user=pg_credentials["user"],
        password=pg_credentials["password"],
        query = """
            CREATE TABLE IF NOT EXISTS ods.users (
                user_id bigserial PRIMARY KEY,
                created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
                username TEXT NULL,
                password TEXT NULL,
                firstname TEXT NULL,
                lastname TEXT NULL,
                email TEXT NULL,
                country TEXT NULL,
                city TEXT NULL
            );
        """
    )