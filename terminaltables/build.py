"""Combine cells into rows."""


def combine(line, left, center, right):
    """Insert borders into list items.

    e.g. ('l', 'a', 'm', 'b', 'm', 'c', 'r')

    :param iter line: List to iterate.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.

    :return: Yields combined objects.
    """
    # Yield left border.
    if left:
        yield left

    # Yield items with center borders.
    if center:
        try:
            for j, i in enumerate(line, start=-len(line) + 1):
                yield i
                if j:
                    yield center
        except TypeError:  # Generator.
            try:
                item = next(line)
            except StopIteration:  # Was empty all along.
                pass
            else:
                while True:
                    yield item
                    try:
                        peek = next(line)
                    except StopIteration:
                        break
                    yield center
                    item = peek
    else:
        for i in line:
            yield i

    # Yield right border.
    if right:
        yield right


def build_row(row, left, center, right):
    """Combine single or multi-lined cells into a single row of list of lists including borders.

    Row must already be padded and extended so each cell has the same number of lines.

    :param iter row: List of cells for one row.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.

    :return: String representation of a row.
    :rtype: list
    """
    combined = list()
    for row_index in range(len(row[0])):
        combined.append(list(combine((c[row_index] for c in row), left, center, right)))
    return combined


def flatten(table):
    """Flatten table data into a single string with newlines.

    :param iter table: Padded and bordered table data.

    :return: Joined rows/cells.
    :rtype: str
    """
    return '\n'.join(''.join(r) for r in table)
