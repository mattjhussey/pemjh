""" Challenge083 """
from __future__ import with_statement


def get_grid(rows):
    """ Read from file """
    grid = []
    for line in [x.strip() for x in rows]:
        next_line = []
        for i in [int(i) for i in line.split(",")]:
            next_line.append(i)
        grid.append(next_line)

    return grid


def main(rows):
    """ challenge083 """
    # Get grid
    grid = get_grid(rows)

    height = len(grid)
    width = len(grid[0])

    # Convert each square to [score, shortest, closed], shortest = None
    grid = [[[square, None, False] for square in row] for row in grid]
    grid[0][0][1] = grid[0][0][0]

    to_process = [[0, 0, grid[0][0]]]

    while to_process:

        # Get next to process
        x_coord, y_coord, square = to_process[0]
        to_process.pop(0)

        # Get surrounding nodes that aren't closed
        neighbours = [[nx_coord, ny_coord]
                      for nx_coord, ny_coord in
                      [[x_coord - 1, y_coord],
                       [x_coord + 1, y_coord],
                       [x_coord, y_coord - 1],
                       [x_coord, y_coord + 1]]
                      if 0 <= nx_coord < width and
                      0 <= ny_coord < height and
                      grid[ny_coord][nx_coord][2] is False]

        for nx_coord, ny_coord in neighbours:
            new_square = grid[ny_coord][nx_coord]

            # Get total from the current spot
            new_length = square[1] + new_square[0]

            # Does this update the current square?
            if not new_square[1]:
                new_square[1] = new_length
                # Newly started square, add to to_process
                to_process.append([nx_coord, ny_coord, new_square])

        square[2] = True

        # Sort the to_process
        to_process.sort(key=lambda x: x[2][1])

    return grid[height - 1][width - 1][1]
