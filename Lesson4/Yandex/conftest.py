import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="This is request url"
    )
#


@pytest.fixture
def url(request):
    return request.config.getoption(name="--url")
#


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
#
