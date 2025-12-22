from typing import Any

def generate_fields_from_dict(dict_row: dict[str, Any]) -> str:
    """
    Генерирует строку с колонками для встравки

    :param dict_row: Словарь, ключи которого являются колонками для вставки в таблицу.
    :return: str, состоящий из списка полей для вставки в таблицу.
    """
    if not dict_row:
        return ""
    return ", ".join(dict_row.keys())


def generate_fields_from_dict_in_placeholder(dict_row: dict[str, Any]) -> str:
    """
    Функция, которая формирует строку, в которой каждое поле обернуто в placeholder.

    :param dict_row:
    :return:
    """
    if not dict_row:
        return ""
    return ", ".join([f"%({k})s" for k in dict_row.keys()])