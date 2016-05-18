"""Test function in module."""

import pytest

from terminaltables.build import build_border


@pytest.mark.parametrize('column_widths,filler,left,center,right,expected', [
    [(5, 6, 7), '-', '<', '+', '>', ('<', '-----', '+', '------', '+', '-------', '>')],
    [(1, 1, 1), '-', '', '', '', ('-', '-', '-')],
    [(1, 1, 1), '', '', '', '', ('', '', '')],
    [(1,), '-', '<', '+', '>', ('<', '-', '>')],
    [(), '-', '<', '+', '>', ('<', '>')],
])
def test_no_title(column_widths, filler, left, center, right, expected):
    """Test without title.

    :param iter column_widths: List of integers representing column widths.
    :param str filler: Character to stretch across each column.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    actual = build_border(column_widths, filler, left, center, right)
    assert actual == expected
