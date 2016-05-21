"""Combine cells into rows."""

from terminaltables.width_and_alignment import truncate


def combine(line, left, center, right):
    """Zip borders between list items.

    e.g. ('l', '1', 'c', '2', 'c', '3', 'r')

    :param iter line: List to iterate.
    :param left: Left border.
    :param center: Column separator.
    :param right: Right border.

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


def build_border(column_widths, filler, left, center, right, title=None):
    """Build the top/bottom/middle row. Optionally embed the table title within the border.

    Title is truncated to fit in between left/right characters.

    Example return value:
    ('<', '-----', '+', '------', '+', '-------', '>')
    ('<', 'My Table', '----', '+', '------->')

    :param iter column_widths: List of integers representing column widths.
    :param str filler: Character to stretch across each column.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.
    :param str title: Overlay the title on the border between the left and right characters.

    :return: Prepared border as a tuple of strings.
    :rtype: tuple
    """
    if not title or not column_widths:
        return tuple(combine((filler * c for c in column_widths), left, center, right))

    fitted_title, length = truncate(title, sum(column_widths) + len(center) * (len(column_widths) - 1))
    columns = list()

    for width in column_widths:
        if length < 1:  # Title is done.
            columns.append(filler * width)
        elif not width:  # 0 character column.
            continue
        elif width >= length:  # Concatenate fillers to title.
            columns.append(fitted_title + filler * (width - length))
            length = 0
        else:  # Column too narrow.
            length -= width

    return tuple(combine(columns, left, center, right))


def build_row(row, left, center, right):
    """Combine single or multi-lined cells into a single row of list of lists including borders.

    Row must already be padded and extended so each cell has the same number of lines.

    Example return value:
    [
        ['>', 'Left ', '|', 'Center', '|', 'Right', '<'],
        ['>', 'Cell1', '|', 'Cell2 ', '|', 'Cell3', '<'],
    ]

    :param iter row: List of cells for one row.
    :param str left: Left border.
    :param str center: Column separator.
    :param str right: Right border.

    :return: Prepared row as a list of tuple of strings.
    :rtype: tuple
    """
    combined = list()
    for row_index in range(len(row[0])):
        combined.append(tuple(combine((c[row_index] for c in row), left, center, right)))
    return combined


def flatten(table):
    """Flatten table data into a single string with newlines.

    :param iter table: Padded and bordered table data.

    :return: Joined rows/cells.
    :rtype: str
    """
    return '\n'.join(''.join(r) for r in table)
