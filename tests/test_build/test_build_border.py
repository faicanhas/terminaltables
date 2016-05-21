# coding: utf-8
"""Test function in module."""

import pytest

from terminaltables.build import build_border


@pytest.mark.parametrize('column_widths,filler,left,center,right,expected', [
    ([5, 6, 7], '-', '<', '+', '>', '<-----+------+------->'),
    ([1, 1, 1], '-', '', '', '', '---'),
    ([1, 1, 1], '', '', '', '', ''),
    ([1], '-', '<', '+', '>', '<->'),
    ([], '-', '<', '+', '>', '<>'),
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
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,center,expected', [
    ([20], '+', 'Applications--------'),
    ([20], '', 'Applications--------'),

    ([15, 5], '+', 'Applications---+-----'),
    ([15, 5], '', 'Applications--------'),

    ([12], '+', 'Applications'),
    ([12], '', 'Applications'),

    ([12, 1], '+', 'Applications+-'),
    ([12, 1], '', 'Applications-'),

    ([12, 0], '+', 'Applications+'),
    ([12, 0], '', 'Applications'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_first_column_fit(column_widths, left, center, right, expected):
    """Test with title that fits in the first column.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, center, right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,expected', [
    ([20], 'Applications--------'),
    ([10, 10], 'Applications--------'),
    ([5, 5, 5, 5], 'Applications--------'),
    ([3, 2, 3, 2, 3, 2, 3, 2], 'Applications--------'),
    ([1] * 20, 'Applications--------'),
    ([10, 5], 'Applications---'),
    ([9, 5], 'Applications--'),
    ([8, 5], 'Applications-'),
    ([7, 5], 'Applications'),
    ([6, 5], 'Application'),
    ([5, 5], 'Applicatio'),
    ([5, 4], 'Applicati'),
    ([4, 4], 'Applicat'),
    ([4, 3], 'Applica'),
    ([3, 3], 'Applic'),
    ([3, 2], 'Appli'),
    ([2, 2], 'Appl'),
    ([2, 1], 'App'),
    ([1, 1], 'Ap'),
    ([1, 0], 'A'),
    ([0, 0], ''),
    ([1], 'A'),
    ([0], ''),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_no_center(column_widths, left, right, expected):
    """Test with no column dividers.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, '', right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,expected', [
    ([20], 'Applications--------'),
    ([0, 20], 'Applications---------'),
    ([20, 0], 'Applications--------+'),
    ([0, 0, 20], 'Applications----------'),
    ([20, 0, 0], 'Applications--------++'),

    ([10, 10], 'Applications---------'),
    ([11, 9], 'Applications---------'),
    ([12, 8], 'Applications+--------'),
    ([13, 7], 'Applications-+-------'),

    ([5, 5, 5, 5], 'Applications-----+-----'),
    ([4, 4, 6, 6], 'Applications----+------'),
    ([3, 3, 7, 7], 'Applications---+-------'),
    ([2, 2, 7, 9], 'Applications-+---------'),
    ([1, 1, 9, 9], 'Applications-+---------'),

    ([2, 2, 2, 2, 2, 2, 2], 'Applications--+--+--'),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'Applications-+-+-+-'),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Applications++++++++'),

    ([2, 2, 2, 2], 'Application'),
    ([1, 1, 1, 1, 1], 'Applicati'),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Applicati'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_center(column_widths, left, right, expected):
    """Test with column dividers.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, '+', right, title='Applications')
    assert ''.join(actual) == expected


@pytest.mark.parametrize('column_widths,center,expected', [
    ([12], '+', u'蓝色--------'),
    ([12], '', u'蓝色--------'),
    ([7, 5], '+', u'蓝色---+-----'),
    ([7, 5], '', u'蓝色--------'),
    ([4], '+', u'蓝色'),
    ([4], '', u'蓝色'),
    ([4, 1], '+', u'蓝色+-'),
    ([4, 1], '', u'蓝色-'),
    ([4, 0], '+', u'蓝色+'),
    ([4, 0], '', u'蓝色'),
    ([12], '', u'蓝色--------'),
    ([6, 6], '', u'蓝色--------'),
    ([3, 3, 3, 3], '', u'蓝色--------'),
])
@pytest.mark.parametrize('left,right', [('', ''), ('<', '>')])
def test_cjk_even(column_widths, left, center, right, expected):
    """Test with CJK characters in title with even number of visible spaces.

    :param iter column_widths: List of integers representing column widths.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.
    :param str expected: Expected output.
    """
    if left and right:
        expected = left + expected + right
    actual = build_border(column_widths, '-', left, center, right, title='蓝色')
    assert ''.join(actual) == expected


@pytest.mark.skipif('True')
def test_rtl():
    """Test with RTL characters in title."""
    pass


@pytest.mark.skipif('True')
def test_colors():
    """Test with color title characters."""
    pass
