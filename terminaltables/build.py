"""Combine cells into rows."""


def next_end(iterator):
    """Yield objects in iterator and detect if the current one is the last.

    :param iter iterator: Object to iterate.

    :return: If there are more items and yield current item.
    :rtype: tuple
    """
    gen = iter(iterator)
    item = next(gen)

    while True:
        try:
            peek = next(gen)
        except StopIteration:
            yield False, item
            raise StopIteration
        yield True, item
        item = peek


def combine(line, left, middle, right):
    """Insert borders into list items.

    e.g. ('l', 'a', 'm', 'b', 'm', 'c', 'r')

    :param iter line: List to iterate.
    :param str left: Left border.
    :param str middle: Column separator.
    :param str right: Right border.

    :return: Yields combined objects.
    """
    # Yield left border.
    if left:
        yield left

    # Yield items with middle borders.
    if middle:
        try:
            for j, i in enumerate(line, start=-len(line) + 1):
                yield i
                if j:
                    yield middle
        except TypeError:  # Generator.
            for j, i in next_end(line):
                yield i
                if j:
                    yield middle
    else:
        for i in line:
            yield i

    # Yield right border.
    if right:
        yield right


def build_row(cells, left, middle, right):
    """Combine single or multi-lined cells into a single row of list of lists including borders.

    Row must already be padded and extended so each cell has the same number of lines.

    :param iter cells: List of cells for one row.
    :param str left: Left border.
    :param str middle: Column separator.
    :param str right: Right border.

    :return: String representation of a row.
    :rtype: list
    """
    combined = list()
    for row_index in range(len(cells)):
        combined.append(list(combine((c[row_index] for c in cells), left, middle, right)))
    return combined


def flatten(table):
    """Flatten table data into a single string with newlines.

    :param iter table: Padded and bordered table data.

    :return: Joined rows/cells.
    :rtype: str
    """
    return '\n'.join(''.join(r) for r in table)
