import pytest
import random


class TestList:

    def test_append_to_empty_list(self):
        test_list = list()
        empty_list_length = len(test_list)
        assert empty_list_length == 0
        test_list.append(1)
        list_length = len(test_list)
        assert list_length - empty_list_length == 1
    #

    def test_append_to_existing_list(self):
        test_list = [1, 2, 3]
        existing_list_length = len(test_list)
        assert existing_list_length > 0
        test_list.append(1)
        list_length = len(test_list)
        assert list_length - existing_list_length == 1
    #

    @pytest.mark.parametrize(
        argnames="builtin_type",
        argvalues=[
            (True, bool),                           # boolean
            (1, int),                               # integer
            (1.2345, float),                        # float
            (complex("1+2j"), complex),             # complex number
            ("1\n\t2", str),                        # string
            ([1, 2, 3], list),                      # list
            (("one", 2), tuple),                    # tuple
            (range(1, 2, 100), range),              # range
            ({1, 2, 3}, set),                       # set
            (frozenset({1, 2, 3}), frozenset),      # frozen set
            (bytes(b"bytes"), bytes),               # bytes
            (bytearray(b"Hello"), bytearray),       # byte array
            (memoryview(b'abcefg'), memoryview),    # memory view
            ({"key": "value"}, dict)                # dictionary
        ])
    def test_append_builtin_types(self, builtin_type):
        test_list = list()
        test_list.append(builtin_type[0])
        assert isinstance(test_list[-1], builtin_type[1])
    #

    def test_pop_at_index(self):
        test_list = [x for x in range(1, 100)]
        length_before_pop = len(test_list)
        random_index = random.randint(0, length_before_pop-1)
        test_list.pop(random_index)
        length_after_pop = len(test_list)
        assert length_before_pop - length_after_pop == 1
    #

    def test_pop_without_index(self):
        test_list = [x for x in range(1, 100)]
        length_before_pop = len(test_list)
        last_element_before_pop = test_list[-1]
        popped_element = test_list.pop()
        assert popped_element == last_element_before_pop
        length_after_pop = len(test_list)
        assert length_before_pop - length_after_pop == 1
#
