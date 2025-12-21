from typing import Any


def return_value(value: Any) -> Any:
    """
    Return value
    :param value: Any
    :return: Any
    """
    return value


def return_only_int(value: int | None = None) -> int | None:
    """
    Return only int
    :param value: int
    :return: int
    """
    if value is not None and not isinstance(value, int):
        raise TypeError(f"Expected int but got {type(value)}.")
    return value