""" Challenge150 """
import sys


def find_smallest_triangle_sum(triangle):
    rows = triangle.get_rows()
    lowest_found = sys.maxint

    # Move starting point to every position and add each row down
    head_row_limit = rows - 1
    for head_row_index in xrange(head_row_limit):
        values_in_head_row = head_row_index + 1
        for head_column_index in xrange(values_in_head_row):
            rows_remaining = rows - head_row_index - 1
            total = triangle.get_sum(head_row_index, head_column_index, 1)
            for row_step in xrange(rows_remaining):
                read_row = head_row_index + row_step + 1
                read_length = row_step + 2
                row_total = triangle.get_sum(read_row, head_column_index, read_length)
                total += row_total
                if total < lowest_found:
                    lowest_found = total
    return lowest_found


class Triangle(object):
    def __init__(self):
        self.__num_rows = 1000
        self.__sums = {}
        t = 0
        value1 = 6159491
        value2 = 797807
        for row_index in xrange(self.__num_rows):
            entities_in_this_row = row_index + 1
            total = 0
            for column in xrange(entities_in_this_row):
                t = (value1 * t + value2) % 2**20
                value = t - 2**19
                total += value
                coordinate = (row_index, column)
                self.__sums[coordinate] = total
        
    def get_rows(self):
        """ Get the number of rows. """
        return self.__num_rows

    def get_sum(self, row, begin_index, length):
        """ Get the sum of a length of numbers. """
        right_hand_side_index = begin_index + length - 1
        right_coordinate = (row, right_hand_side_index)
        right_hand_sum = self.__sums[right_coordinate]

        if begin_index == 0:
            return right_hand_sum
        else:
            left_hand_side_index = begin_index - 1
            left_coordinate = (row, left_hand_side_index)
            left_hand_sum = self.__sums[left_coordinate]
            total = right_hand_sum - left_hand_sum
            return total


def main():
    """ challenge150 """
    return find_smallest_triangle_sum(Triangle())
