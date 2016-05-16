"""Test functions in module."""

import pytest

from terminaltables.build import combine


@pytest.mark.parametrize('generator', [False, True])
def test_combine(generator):
    """Test function.

    :param bool generator: Test with generator instead of list.
    """
    line = ('One', 'Two', 'Three')

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
