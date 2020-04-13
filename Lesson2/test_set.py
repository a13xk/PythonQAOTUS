import pytest


class TestSet:

    def test_add_to_empty_set(self):
        test_set = set()
        empty_set_length = len(test_set)
        assert empty_set_length == 0
        test_set.add(1)
        set_length = len(test_set)
        assert set_length - empty_set_length == 1
    #

    def test_add_missing_element_to_existing_set(self):
        test_set = {1, 2, 3}
        missing_value = 4
        assert missing_value not in test_set
        existing_set_length = len(test_set)
        assert existing_set_length > 0
        test_set.add(missing_value)
        set_length = len(test_set)
        assert set_length - existing_set_length == 1
    #

    def test_add_existing_element_to_existing_set(self):
        test_set = {1, 2, 3}
        existing_value = 1
        assert existing_value in test_set
        existing_set_length = len(test_set)
        assert existing_set_length > 0
        test_set.add(existing_value)
        set_length = len(test_set)
        assert set_length == existing_set_length
    #

    @pytest.mark.parametrize(
        argnames="builtin_immutable_type",
        argvalues=[
            (True, bool),                           # boolean
            (1, int),                               # integer
            (1.2345, float),                        # float
            (complex("1+2j"), complex),             # complex number
            ("1\n\t2", str),                        # string
            (("one", 2), tuple),                    # tuple
            (range(1, 2, 100), range),              # range
            (frozenset({1, 2, 3}), frozenset),      # frozen set
            (bytes(b"bytes"), bytes),               # bytes
            (memoryview(b'abcefg'), memoryview)     # memory view
        ])
    def test_add_builtin_immutable_types(self, builtin_immutable_type):
        test_set = set()
        test_set.add(builtin_immutable_type[0])
        test_element = next(iter(test_set))
        assert isinstance(test_element, builtin_immutable_type[1])
    #

    @pytest.mark.parametrize(
        argnames="builtin_mutable_type",
        argvalues=[
            [1, 2, 3],              # list
            {1, 2, 3},              # set
            bytearray(b"Hello"),    # byte array
            {"key": "value"}        # dictionary
        ])
    def test_add_builtin_mutable_types(self, builtin_mutable_type):
        test_set = set()
        with pytest.raises(TypeError):
            test_set.add(builtin_mutable_type)
    #
#
