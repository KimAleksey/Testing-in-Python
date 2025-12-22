from pathlib import Path

from dotenv import load_dotenv
from os import getenv

from handles.oltp.execute_custom_query import execute_custom_query

if __name__ == "__main__":

    # Получаем путь до файла с реквизитами подключения к PG
    BASE_DIR = Path(__file__).resolve().parents[2]
    env_path = BASE_DIR / "config" / ".env"

    # Получаем реквизиты
    load_dotenv(dotenv_path=env_path)

    db_name = getenv("POSTGRES_DB")
    host = getenv("POSTGRES_HOST")
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    port = getenv("POSTGRES_PORT")

    execute_custom_query(
        db_name=db_name,
        host=host,
        user=user,
        password=password,
        port=port,
        query = """
            CREATE SCHEMA IF NOT EXISTS users;
        """
    )