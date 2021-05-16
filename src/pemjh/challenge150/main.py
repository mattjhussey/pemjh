""" Challenge150 """
import numpy as np


def main():
    """ challenge150 """
    rows = 1000
    targ, row, col = 0, 0, 0
    triang = np.zeros([rows, rows])
    for _ in range(rows*(rows+1)//2):
        targ = (615949*targ + 797807) % 2**20
        triang[row, col] = targ - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0

    triang1 = np.zeros([rows, rows])
    triang2 = np.zeros([rows, rows])
    min_init = np.min(triang)

    triang_new = np.zeros([rows+1, rows+1])
    for row2 in range(2, rows):
        triang_new = np.zeros([rows, rows])
        for row in range(rows-row2):
            triang_new[row, :row+1] = triang[row, :row+1] + \
                                      triang2[row+1, :row+1] + \
                                      triang2[row+1, 1:row+2] - \
                                      triang1[row+2, 1:row+2]
        row_min = np.min(triang_new)
        min_init = min(min_init, row_min)
        triang1 = triang2
        triang2 = triang_new

    return min_init
