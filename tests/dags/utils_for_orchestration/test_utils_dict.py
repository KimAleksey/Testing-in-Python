import pytest

from utils_for_orchestration.utils_dict import generate_fields_from_dict
from utils_for_orchestration.utils_dict import generate_fields_from_dict_in_placeholder

class TestGenerateFieldsFromDict:
    def test_empty(self):
        assert generate_fields_from_dict({}) == ""

    def test_none(self):
        assert generate_fields_from_dict(None) == ""

    def test_not_dict(self):
        with pytest.raises(TypeError):
            generate_fields_from_dict([1, 2, 3])

    def test_correct_dict(self):
        result = generate_fields_from_dict({"a": 1, "b": 2, "c": 3})
        assert result == "a, b, c"


class TestGenerateFieldsFromDictInPlaceholder:
    def test_empty(self):
        assert generate_fields_from_dict_in_placeholder({}) == ""

    def test_none(self):
        assert generate_fields_from_dict_in_placeholder(None) == ""

    def test_not_dict(self):
        with pytest.raises(TypeError):
            generate_fields_from_dict_in_placeholder([1, 2, 3])

    def test_correct_dict(self):
        result = generate_fields_from_dict_in_placeholder({"a": 1, "b": 2, "c": 3})
        assert result == "%(a)s, %(b)s, %(c)s"