import requests


def test_function(url, status_code):
    res = requests.get(url=url)
    assert res.status_code == int(status_code)
#
