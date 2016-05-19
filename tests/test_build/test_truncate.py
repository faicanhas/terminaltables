# coding: utf-8
"""Test function in module."""

import pytest
from colorama import Fore
from colorclass import Color

from terminaltables.build import truncate


@pytest.mark.parametrize('string,max_length,expected_str,expected_len', [
    ('TEST', 2, 'TE', 2),
    ('TEST', 0, '', 0),
    ('TEST', 5, 'TEST', 4),
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


@pytest.mark.parametrize('string,max_length,expected_str,expected_len', [
    ('世界你好', 8, u'世界你好', 8),
    ('世界你好', 4, u'世界', 4),
    ('世界你好', 3, u'世', 2),
    ('a世界你好', 3, u'a世', 3),
    ('שלום', 4, u'שלום', 4),
    ('שלום', 3, u'שלו', 3),
    ('معرب', 4, u'معرب', 4),
    ('معرب', 3, u'معر', 3),
])
def test_cjk_rtl(string, max_length, expected_str, expected_len):
    """Test with CJK and RTL characters.

    :param str string: String to operate on.
    :param int max_length: Truncate to this size.
    :param str expected_str: Expected truncated string.
    :param int expected_len: Expected truncated string size.
    """
    actual_str, actual_len = truncate(string, max_length)
    assert actual_str == expected_str
    assert actual_len == expected_len


@pytest.mark.parametrize('string,max_length,expected_str,expected_len', [
    # str+ansi
    ('\x1b[34mTEST\x1b[39m', 4, '\x1b[34mTEST\x1b[39m', 4),
    ('\x1b[34mTEST\x1b[39m', 2, '\x1b[34mTE\x1b[39m', 2),
    ('\x1b[34mT\x1b[35mE\x1b[36mS\x1b[37mT\x1b[39m', 2, '\x1b[34mT\x1b[35mE\x1b[36m\x1b[37m\x1b[39m', 2),
    ('\x1b[34m世界\x1b[39m', 4, u'\x1b[34m世界\x1b[39m', 4),
    ('\x1b[34m世界\x1b[39m', 2, u'\x1b[34m世\x1b[39m', 2),
    ('\x1b[34m世\x1b[35m界\x1b[39m', 2, u'\x1b[34m世\x1b[35m\x1b[39m', 2),

    # colorclass
    (Color('{blue}TEST{/blue}'), 4, '\x1b[34mTEST\x1b[39m', 4),
    (Color('{blue}TEST{/blue}'), 2, '\x1b[34mTE\x1b[39m', 2),
    (Color('{blue}T{magenta}E{cyan}S{white}T{/blue}'), 2, '\x1b[34mT\x1b[35mE\x1b[36m\x1b[37m\x1b[39m', 2),
    (Color(u'{blue}世界{/blue}'), 4, u'\x1b[34m世界\x1b[39m', 4),
    (Color(u'{blue}世界{/blue}'), 2, u'\x1b[34m世\x1b[39m', 2),
    (Color(u'{blue}世{magenta}界{/blue}'), 2, u'\x1b[34m世\x1b[35m\x1b[39m', 2),

    # colorama
    (Fore.BLUE + 'TEST' + Fore.RESET, 4, '\x1b[34mTEST\x1b[39m', 4),
    (Fore.BLUE + 'TEST' + Fore.RESET, 2, '\x1b[34mTE\x1b[39m', 2),
    (
        Fore.BLUE + 'T' + Fore.MAGENTA + 'E' + Fore.CYAN + 'S' + Fore.WHITE + 'T' + Fore.RESET,
        2,
        '\x1b[34mT\x1b[35mE\x1b[36m\x1b[37m\x1b[39m', 2
    ),
    (Fore.BLUE + '世界' + Fore.RESET, 4, u'\x1b[34m世界\x1b[39m', 4),
    (Fore.BLUE + '世界' + Fore.RESET, 2, u'\x1b[34m世\x1b[39m', 2),
    (Fore.BLUE + '世' + Fore.MAGENTA + '界' + Fore.RESET, 2, u'\x1b[34m世\x1b[35m\x1b[39m', 2),
])
def test_colors(string, max_length, expected_str, expected_len):
    """Test with color characters.

    :param str string: String to operate on.
    :param int max_length: Truncate to this size.
    :param str expected_str: Expected truncated string.
    :param int expected_len: Expected truncated string size.
    """
    actual_str, actual_len = truncate(string, max_length)
    assert actual_str == expected_str
    assert actual_len == expected_len
