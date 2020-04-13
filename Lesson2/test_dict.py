import random
import string

import pytest


def generate_random_string(string_length: int):
    """
    Helper method to generate random string value
    :param string_length: Length of random string
    """
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(string_length)])
#


class TestDict:

    def test_get_existing_key(self):
        test_dict = dict()
        key = "key"
        value = "value"
        test_dict[key] = value

        assert test_dict.get(key) == value
    #

    def test_get_missing_key(self):
        test_dict = dict()
        missing_key = "missing key"
        assert test_dict.get(missing_key) is None
    #

    def test_setdefault_existing_key(self):
        test_dict = dict()
        key = "key"
        existing_value = "existing value"
        default_value = "default value"
        test_dict[key] = existing_value

        assert test_dict.setdefault(key, default_value) == existing_value
    #

    def test_setdefault_missing_key(self):
        test_dict = dict()
        missing_key = "missing key"
        default_value = "default value"

        assert test_dict.setdefault(missing_key, default_value) == default_value
    #

    @pytest.mark.parametrize(
        argnames="keys",
        argvalues=[
            ["one", "two", "three"],
            {1, 2, 3},
            (None, complex("1+2j"), bytes(b"bytes"))
        ])
    def test_fromkeys(self, keys):
        value = generate_random_string(random.randint(1, 100))
        test_dict = dict.fromkeys(keys, value)
        for k in keys:
            assert k in test_dict.keys()
#
