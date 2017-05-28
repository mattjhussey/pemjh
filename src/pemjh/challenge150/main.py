""" Challenge150 """
import numpy as np


def main():
    """ challenge150 """
    rows = 1000
    t, row, col = 0, 0, 0
    Triang = np.zeros([rows, rows])
    for k in range(rows*(rows+1)/2):
        t = (615949*t + 797807)%2**20
        Triang[row, col] = t - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0
   
    Triang1 = np.zeros([rows, rows])
    Triang2 = np.zeros([rows, rows])
    min_init = np.min(Triang)

    Triang_new = np.zeros([rows+1, rows+1])
    for n in range(2,rows):
        Triang_new = np.zeros([rows, rows])
        for row in range(rows-n):
            Triang_new[row, :row+1] = Triang[row, :row+1] + Triang2[row+1, :row+1] + \
                                      Triang2[row+1, 1:row+2] - Triang1[row+2, 1:row+2] 
        row_min = np.min(Triang_new)
        if min_init > row_min:
            min_init = row_min 
        Triang1 = Triang2
        Triang2 = Triang_new

    return min_init
