""" Challenge022 """
from __future__ import with_statement


def get_names(raw_names):
    """
    >>> get_names(['"Gary","Barry","Fred"', '"Alice","Stuart"'])
    ['Alice', 'Barry', 'Fred', 'Gary', 'Stuart']
    """
    names = []
    # Read in the file
    for next_line in raw_names:
        # Split into comma separated
        for name in next_line.split(","):
            # Strip quotes
            names.append(name.strip("\""))
    names.sort()
    return names


def scored_names(sorted_names):
    """
    >>> list(scored_names(['ALICE', 'BARRY', 'FRED']))
    [30, 128, 99]
    """
    line = 1
    origin = ord("A") - 1
    for name in sorted_names:
        score = 0
        for character in name:
            score += ord(character) - origin
        yield score * line
        line += 1


def main(names):
    """ challenge022 """
    total = 0
    for score in scored_names(get_names(names)):
        total += score

    return total
