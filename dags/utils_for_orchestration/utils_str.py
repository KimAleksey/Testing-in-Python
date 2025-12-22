def generate_insert_into_for_row(
        schema: str | None = "public",
        table: str | None = None,
        columns: str | None = None,
        placeholders: str | None = None,
) -> str:
    """
    Функция, которая генерирует строку для генерации запроса INSERT в Postgres

    :param schema: Схема БД
    :param table: Таблица БД
    :param columns: Колонки для вставки
    :param placeholders: Колонки обернутые в плейсхолдеры
    :return: str - сгенерированный запрос на INSERT
    """
    return f"INSERT INTO {schema}.{table} ({columns}) VALUES ({placeholders});"