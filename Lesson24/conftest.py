import pytest
import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url, на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address
    #

    def post(self, path="/", params=None, data=None, headers=None) -> requests.Response:
        url = self.base_address + path
        print(f"POST request to {url}")
        return requests.post(url=url, params=params, data=data, headers=headers)
    #

    def get(self, path="/", params=None) -> requests.Response:
        url = self.base_address + path
        print(f"GET request to {url}")
        return requests.get(url=url, params=params)
    #
#


# Тестовый API: https://dog.ceo/dog-api/
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo/api",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
#
