from typing import Any

import requests


def get_data_from_api(url: str, time_out: int = 600) -> dict[Any, Any]:
    """
    Get data from API. URL must be non-empty string.
    :param url: URL to get data from.
    :param time_out: Timeout in seconds.
    :return: JSON of response.
    """
    if not isinstance(url, str):
        raise TypeError(f"Expected str but got {type(url)}.")
    if not url:
        raise TypeError(f"URL should not be empty.")

    try:
        request = requests.get(url=url, timeout=time_out)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed extract data from {url}: {e}")

    if request.status_code != 200:
        raise RuntimeError(f"Failed extract data from {url}: {request.status_code}")

    try:
        return request.json()
    except Exception as exc:
        raise Exception(f"Ошибка в парсинге JSON из ответа {url}: {exc}")