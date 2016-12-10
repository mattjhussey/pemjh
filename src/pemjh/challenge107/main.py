""" Challenge107 """
from __future__ import with_statement


def skim_network(grid):
    # Choose row A as the first working row
    connected_rows = [0]
    available_connections = sorted([(l, 0, i) for i, l in enumerate(grid[0])
                                    if l > 0])
    connections = list()

    # While there are available connections
    while len(available_connections) > 0:
        # Get shortest available connection
        shortest = available_connections[0]

        # Add as a connected row
        connected_rows.append(shortest[2])

        # Add the connection
        connections.append(shortest)

        # Remove any from available_connections that go to a destination
        available_connections = [link for link in available_connections
                                 if link[2] not in connected_rows]

        # Add the target row to the available connections
        available_connections.extend([(l, shortest[2], i)
                                      for i, l in enumerate(grid[shortest[2]])
                                      if l > 0 and i not in connected_rows])

        available_connections.sort()

    # Create the new grid
    new_grid = [[0] * len(grid) for _ in grid]
    for connection in connections:
        new_grid[connection[1]][connection[2]] = connection[0]
        new_grid[connection[2]][connection[1]] = connection[0]
    return new_grid


def score_grid(grid):
    total = 0
    offset = 1
    # Loop through rows
    for row in grid[:-1]:
        for value in row[offset:]:
            total += value
        offset += 1

    return total


def main(grid):
    """ challenge107 """

    # Score the grid in its current state
    original_score = score_grid(grid)

    # Shorten the grid to only essentials
    new_grid = skim_network(grid)

    # Score the new grid
    new_score = score_grid(new_grid)

    # Return original - new
    return original_score - new_score
