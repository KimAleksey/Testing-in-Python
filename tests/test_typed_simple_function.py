import pytest

from main.main import return_only_int


def test_typed_simple_function_int():
    assert return_only_int(5) == 5


def test_typed_simple_function_none():
    assert return_only_int(None) is None


def test_typed_simple_function_str_raises():
    with pytest.raises(TypeError):
        return_only_int("hello")


def test_typed_simpel_function_float_raises():
    with pytest.raises(TypeError):
        return_only_int(1.1)


def test_typed_simpel_function_list_raises():
    with pytest.raises(TypeError):
        return_only_int([1, 2, 3])