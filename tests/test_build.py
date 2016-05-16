"""Test functions in module."""

import pytest

from terminaltables.build import build_row, combine


@pytest.mark.parametrize('generator', [False, True])
def test_combine(generator):
    """Test function.

    :param bool generator: Test with generator instead of list.
    """
    line = ['One', 'Two', 'Three']

    # Test all features.
    actual = list(combine(iter(line) if generator else line, '>', '|', '<'))
    assert actual == ['>', 'One', '|', 'Two', '|', 'Three', '<']

    # Test no borders.
    actual = list(combine(iter(line) if generator else line, '', '', ''))
    assert actual == ['One', 'Two', 'Three']

    # Test no items.
    line = iter([]) if generator else []
    actual = list(combine(iter(line) if generator else line, '>', '|', '<'))
    assert actual == ['>', '<']


def test_build_row_one_line():
    """Test function with one line cells."""
    row = [
        ['Left Cell'], ['Center Cell'], ['Right Cell'],
    ]
    actual = build_row(row, '>', '|', '<')
    expected = [
        ['>', 'Left Cell', '|', 'Center Cell', '|', 'Right Cell', '<'],
    ]
    assert actual == expected


def test_build_row_two_line():
    """Test function with two line cells."""
    row = [
        [
            'Left ',
            'Cell1',
        ],

        [
            'Center',
            'Cell2 ',
        ],

        [
            'Right',
            'Cell3',
        ],
    ]
    actual = build_row(row, '>', '|', '<')
    expected = [
        ['>', 'Left ', '|', 'Center', '|', 'Right', '<'],
        ['>', 'Cell1', '|', 'Cell2 ', '|', 'Cell3', '<'],
    ]
    assert actual == expected


def test_build_row_three_line():
    """Test function with three line cells."""
    row = [
        [
            'Left ',
            'Cell1',
            '     ',
        ],

        [
            'Center',
            'Cell2 ',
            '      ',
        ],

        [
            'Right',
            'Cell3',
            '     ',
        ],
    ]
    actual = build_row(row, '>', '|', '<')
    expected = [
        ['>', 'Left ', '|', 'Center', '|', 'Right', '<'],
        ['>', 'Cell1', '|', 'Cell2 ', '|', 'Cell3', '<'],
        ['>', '     ', '|', '      ', '|', '     ', '<'],
    ]
    assert actual == expected


def test_build_row_single_empty():
    """Test function with single cell and empty cell."""
    # Test single cell.
    actual = build_row([['Cell']], '>', '|', '<')
    expected = [
        ['>', 'Cell', '<'],
    ]
    assert actual == expected

    # Test empty cell.
    actual = build_row([['']], '>', '|', '<')
    expected = [
        ['>', '', '<'],
    ]
    assert actual == expected
