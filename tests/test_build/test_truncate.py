"""Test function in module."""

import pytest

from terminaltables.build import truncate


@pytest.mark.parametrize('string,max_length,expected_str,expected_len', [
    ('Input', 2, 'In', 2),
    ('Input', 0, '', 0),
    ('Input', 6, 'Input', 5),
    ('', 2, '', 0),
    ('', 0, '', 0),
    ('', 6, '', 0),
])
def test_ascii(string, max_length, expected_str, expected_len):
    """Test with ASCII characters only.

    :param str string: String to operate on.
    :param int max_length: Truncate to this size.
    :param str expected_str: Expected truncated string.
    :param int expected_len: Expected truncated string size.
    """
    actual_str, actual_len = truncate(string, max_length)
    assert actual_str == expected_str
    assert actual_len == expected_len
