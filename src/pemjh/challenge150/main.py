""" Challenge150 """
import sys
from pemjh.function_tools import memoize


def find_smallest_triangle_sum(triangle):
    rows = triangle.get_rows()
    lowest_found = sys.maxint

    # Move starting point to every position and add each row down
    # head_row_limit = rows - 1
    for head_row_index in xrange(rows, 0, -1):
        values_in_head_row = head_row_index + 1
        for head_column_index in xrange(values_in_head_row):
            rows_remaining = rows - head_row_index
            for length in xrange(rows_remaining):
                triangle_sum = triangle.get_sum(head_row_index, head_column_index, length + 1)
                lowest_found = min(lowest_found, triangle_sum)
    return lowest_found


class Triangle(object):
    def __init__(self):
        self.__num_rows = 1000
        self.__values = {}
        t = 0
        value1 = 6159491
        value2 = 797807
        for row_index in xrange(self.__num_rows):
            entities_in_this_row = row_index + 1
            for column in xrange(entities_in_this_row):
                t = (value1 * t + value2) % 2**20
                value = t - 2**19
                coordinate = (row_index, column)
                self.__values[coordinate] = value
        
    def get_rows(self):
        """ Get the number of rows. """
        return self.__num_rows

    @memoize()
    def get_sum(self, row, column, length):
        """ Get the sum of a length of numbers. """
        top_coordinate = (row, column)
        if length == 1:
            return self.__values[top_coordinate]
        if length == 2:
            left_coordinate = (row + 1, column)
            right_coordinate = (row + 1, column + 1)
            return self.__values[top_coordinate] + \
                self.__values[left_coordinate] + \
                self.__values[right_coordinate]
        return self.__values[top_coordinate] + \
            self.get_sum(row + 1, column, length - 1) + \
            self.get_sum(row + 1, column + 1, length - 1) - \
            self.get_sum(row + 2, column + 1, length - 2)


def main():
    """ challenge150 """
    return find_smallest_triangle_sum(Triangle())
