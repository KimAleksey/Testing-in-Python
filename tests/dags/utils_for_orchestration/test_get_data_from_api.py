import pytest
from unittest.mock import MagicMock, patch
from dags.utils_for_orchestration.utils_api import get_data_from_api


class TestGetDataFromAPI:
    URL = "https://api.example.com/api"

    @patch("dags.utils_for_orchestration.utils_api.requests.get")
    def test_successful_get(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok", "data": [1, 2, 3]}

        mock_request.return_value = mock_response

        result = get_data_from_api(TestGetDataFromAPI.URL)

        mock_request.assert_called_with(url=TestGetDataFromAPI.URL, timeout=600)
        assert result == {"status": "ok", "data": [1, 2, 3]}

    def test_empty_url(self):
        with pytest.raises(TypeError):
            get_data_from_api("")

    def test_url_not_str(self):
        with pytest.raises(TypeError):
            get_data_from_api(123)

    @patch("dags.utils_for_orchestration.utils_api.requests.get")
    def test_status_code_not_ok(self, mock_request):
        error_code = 404
        mock_response = MagicMock()
        mock_response.status_code = error_code

        mock_request.return_value = mock_response

        with pytest.raises(
                RuntimeError,
                match=f"Failed extract data from {TestGetDataFromAPI.URL}: {error_code}"
        ):
            get_data_from_api(TestGetDataFromAPI.URL)