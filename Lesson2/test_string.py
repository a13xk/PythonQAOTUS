import random
import pytest
import string


def generate_random_mixed_case_string(string_length: int):
    """
    Helper method to generate random string value with both uppercase and lowercase characters
    :param string_length: Length of random string
    """
    return "".join([random.choice(string.ascii_letters) for _ in range(string_length)])
#


class TestString:

    @pytest.mark.parametrize(argnames="string_length", argvalues=[1, 1000, 100_000])
    def test_lower(self, string_length):
        test_string = generate_random_mixed_case_string(string_length)
        test_string = test_string.lower()
        for c in test_string:
            assert c.islower()
    #

    @pytest.mark.parametrize(argnames="string_length", argvalues=[1, 1000, 100_000])
    def test_upper(self, string_length):
        test_string = generate_random_mixed_case_string(string_length)
        test_string = test_string.upper()
        for c in test_string:
            assert c.isupper()
    #

    def test_split(self):
        separator = ":"
        first = "abc"
        second = "ABC"
        test_string = first + separator + second
        split_string = test_string.split(sep=separator)
        assert len(split_string) == 2
        assert split_string[0] == first
        assert split_string[1] == second
    #

    def test_join(self):
        separator = ":"
        first = "abc"
        second = "ABC"
        test_list = [first, second]
        test_string = separator.join(test_list)
        assert isinstance(test_string, str)
        assert first in test_string
        assert separator in test_string
        assert second in test_string
    #

    @pytest.mark.parametrize(argnames="test_string", argvalues=["123", "abc", ""])
    def test_zfill(self, test_string):
        random_width = len(test_string) + random.randint(1, 5)
        zfilled_test_string = test_string.zfill(random_width)
        assert len(zfilled_test_string) == random_width
        assert "0" in zfilled_test_string
#
