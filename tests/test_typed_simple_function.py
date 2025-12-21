import pytest

from main.main import return_only_int

class TestReturnOnlyInt:
    @pytest.mark.unit
    def test_typed_simple_function_int(self):
        assert return_only_int(5) == 5

    @pytest.mark.unit
    def test_typed_simple_function_none(self):
        assert return_only_int(None) is None

    @pytest.mark.unit
    def test_typed_simple_function_str_raises(self):
        with pytest.raises(TypeError):
            return_only_int("hello")

    @pytest.mark.unit
    def test_typed_simpel_function_float_raises(self):
        with pytest.raises(TypeError):
            return_only_int(1.1)

    @pytest.mark.unit
    def test_typed_simpel_function_list_raises(self):
        with pytest.raises(TypeError):
            return_only_int([1, 2, 3])