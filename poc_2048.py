__author__ = 'jeredyang'

"""
Clone of 2048 game.
"""

# import poc_2048_gui
import poc_simpletest as st

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # 1. Start with a result list that contains the same number of 0's as the length of the line argument.
    re = [0] * len(line)
    last_merged = False

    # 2. Iterate over the line input looking for non-zero entries. For each non-zero entry, put the value into the
    # next available entry of the result list (starting at position 0).
    for entry_index in range(0, len(line)):
        if line[entry_index] != 0:
            for re_index in range(0, len(re)):
                if re[re_index] == 0:
                    re[re_index] = line[entry_index]
                    last_merged = False
                    break
                # if it's not 0
                else:
                    # if the two are the same and the last one was not merged
                    if re[re_index] == line[entry_index] and last_merged is False:
                        re[re_index] = re[re_index] + line[entry_index]
                        last_merged = True
                        break

            continue

    return re

# line = [2, 0, 2, 2]
# test = st.TestSuite()
# test.run_test(merge(line), [2, 2, 2, 0], "Test Merge")

# [2, 0, 2, 4] should return [4, 4, 0, 0]
# [0, 0, 2, 2] should return [4, 0, 0, 0]
# [2, 2, 0, 0] should return [4, 0, 0, 0]
# [2, 2, 2, 2] should return [4, 4, 0, 0]
# [8, 16, 16, 8] should return [8, 32, 8, 0]

# line = [2, 0, 2, 4]
# line_expected = [4, 4, 0, 0]
# test = st.TestSuite()
# test.run_test(merge(line), line_expected, "Test Merge")
#
# line = [0, 0, 2, 2]
# line_expected = [4, 0, 0, 0]
# test = st.TestSuite()
# test.run_test(merge(line), line_expected, "Test Merge")
#
# line = [2, 2, 0, 0]
# line_expected = [4, 0, 0, 0]
# test = st.TestSuite()
# test.run_test(merge(line), line_expected, "Test Merge")
#
# line = [2, 2, 2, 2]
# line_expected = [4, 4, 0, 0]
# test = st.TestSuite()
# test.run_test(merge(line), line_expected, "Test Merge")
#
# line = [8, 16, 16, 8]
# line_expected = [8, 32, 8, 0]
# test = st.TestSuite()
# test.run_test(merge(line), line_expected, "Test Merge")


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        pass

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        pass

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
