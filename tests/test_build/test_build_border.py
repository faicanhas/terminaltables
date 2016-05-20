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


@pytest.mark.parametrize('column_widths,filler,left,center,right,expected', [
    [(9, 8, 7), '-', '<', '+', '>', ('<', 'My Table-', '+', '--------', '+', '-------', '>')],
    [(8, 8, 7), '-', '<', '+', '>', ('<', 'My Table', '+', '--------', '+', '-------', '>')],
    # [(5, 6, 7), '-', '<', '+', '>', ('<', 'My Table', '----', '+', '-------', '>')],
    # [(3, 3, 3), '-', '<', '+', '>', ('<', 'My Table', '---', '>')],
    # [(3, 3, 3), '-', '<', '', '>', ('<', 'My Table', '>')],
    # [(2, 2, 2), '-', '<', '+', '>', ('<', 'My Table', '>')],
    # [(1, 1, 1), '-', '', '', '', ('My ',)],
    # [(1, 1, 1), '', '', '', '', ('',)],
    [(1,), '-', '<', '+', '>', ('<', 'M', '>')],
    [(), '-', '<', '+', '>', ('<', '>')],
])
def test_ascii(column_widths, filler, left, center, right, expected):
    """Test with regular ASCII title.

    :param iter column_widths: List of integers representing column widths.
    :param str filler: Character to stretch across each column.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    actual = build_border(column_widths, filler, left, center, right, title='My Table')
    assert actual == expected


@pytest.mark.skipif('True')
def test_cjk():
    """Test with CJK characters in title."""
    pass


@pytest.mark.skipif('True')
def test_rtl():
    """Test with RTL characters in title."""
    pass


@pytest.mark.skipif('True')
def test_colors():
    """Test with color title characters."""
    pass
