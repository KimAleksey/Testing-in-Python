import pytest

from copy import deepcopy

from dags.utils_for_orchestration.utils_transform import transform_nested_fields


class TestTransformNestedFields:
    CORRECT_DATA = {
        'results':
            [
                {
                    'name': {
                        'first': 'Ellen',
                        'last': 'Tuomala',
                    },
                    'location': {
                        'city': 'Nykarleby',
                        'country': 'Finland',
                    },
                    'email': 'ellen.tuomala@example.com',
                    'login': {
                        'username': 'angryladybug995',
                        'password': 'success',
                    },

                },
            ],
        'info': {
            'seed': 'fa68cbd068c14000',
            'results': 1,
            'page': 1,
            'version': '1.4'
        }
    }

    def test_transform_nested_fields_empty(self):
        data = {}
        with pytest.raises(TypeError):
            transform_nested_fields(data)

    def test_transform_nested_fields_none(self):
        data = None
        with pytest.raises(TypeError):
            transform_nested_fields(data)

    def test_transform_nested_fields_no_key_results(self):
        data = {"foo": 123}
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_is_empty(self):
        data = {"results": []}
        with pytest.raises(IndexError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_no_login(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        data["results"][0].pop('login')
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_no_name(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        data["results"][0].pop('name')
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_no_location(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        data["results"][0].pop('location')
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_no_email(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        data["results"][0].pop('email')
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_results_no_first(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        data["results"][0]["name"].pop('first')
        with pytest.raises(KeyError):
            transform_nested_fields(data)

    def test_transform_nested_fields_correct_data(self):
        data = deepcopy(TestTransformNestedFields.CORRECT_DATA)
        result = transform_nested_fields(data)

        assert result == {
            'username': 'angryladybug995',
            'password': 'success',
            'firstname': 'Ellen',
            'lastname': 'Tuomala',
            'email': 'ellen.tuomala@example.com',
            'country': 'Finland',
            'city': 'Nykarleby'
        }