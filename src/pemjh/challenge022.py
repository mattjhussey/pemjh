""" Challenge022 """
from __future__ import with_statement
from pkgutil import get_data


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


def main():
    """ challenge022 """
    total = 0
    name_file = get_data(__name__, 'names.txt')
    raw_names = [s.strip() for s in name_file.split('\n')]
    for score in scored_names(get_names(raw_names)):
        total += score

    return total
