__author__ = 'jeredyang'

"""
Clone of 2048 game.
"""

# import poc_2048_gui
import poc_simpletest as st
import random

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


def get_ran_num(up_limit):
    """
    randomly pick a row or col number
    :param up_limit: limited by current row or col
    :return:
    """
    num = random.randrange(0, up_limit)
    return num


def gen_num():
    """
    generate a 2 or 4. with 10% chance of getting a 4 and 90% chance of getting a 2
    :return:
    """
    # get the probability
    p = random.random()

    # 10% chance p < 0.1, that's when we return 2
    if p < 0.1:
        return 4
    # otherwise return 2
    else:
        return 2


def get_ini_tiles(wid, hei):
    ini_tiles = {}

    keys = [UP, DOWN, LEFT, RIGHT]

    # generate initial tiles for UP
    for each_key in keys:
        ls = []
        if each_key == UP:
            for w in range(wid):
                ls.append((0, w))
        elif each_key == DOWN:
            for w in range(wid):
                ls.append((hei - 1, w))
        elif each_key == LEFT:
            for w in range(hei):
                ls.append((w, 0))
        else:
            for w in range(hei):
                ls.append((w, wid - 1))

        ini_tiles[each_key] = ini_tiles.get(each_key, ls)

    return ini_tiles

# test_it = get_ini_tiles(3, 3)
# print test_it


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.cells = {}
        self.ini_tiles = get_ini_tiles(self.width, self.height)
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.cells[(row, col)] = self.cells.get((row, col), 0)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for row in range(self.height):
            # literate to 1 element before the end
            for col in range(self.width):
                # this is the end of the line
                if col == self.width - 1:
                    string += str(self.cells[(row, col)]) + "\n"
                # otherwise separated by ", ". so there will be no ", " at the end of each line
                else:
                    string += str(self.cells[(row, col)]) + ", "

        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tile_changed = False

        for each in self.ini_tiles[direction]:
            temp_ls = []

            target_row = each[0]
            target_col = each[1]

            # add cells to the list until the index exceeds
            while (target_row, target_col) in self.cells:
                temp_ls.append(self.cells[(target_row, target_col)])
                target_row += OFFSETS[direction][0]
                target_col += OFFSETS[direction][1]

            # merge the line
            temp_ls = merge(temp_ls)

            # traverse the cells again
            target_row = each[0]
            target_col = each[1]
            ls_index = 0

            # add cells to the list until the index exceeds
            while (target_row, target_col) in self.cells:
                # if the new value is not equal to original value, the tile must have changed
                if self.cells[(target_row, target_col)] != temp_ls[ls_index]:
                    tile_changed = True

                self.cells[(target_row, target_col)] = temp_ls[ls_index]
                target_row += OFFSETS[direction][0]
                target_col += OFFSETS[direction][1]
                ls_index += 1

        # if tile has changed, then must call new_tile
        if tile_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        self.set_tile(get_ran_num(self.height), get_ran_num(self.width), gen_num())

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cells[(row, col)] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.cells[(row, col)]


test_grid = TwentyFortyEight(4, 4)
print test_grid

test_grid.set_tile(0, 0, 4)
test_grid.set_tile(0, 1, 2)
test_grid.set_tile(0, 2, 2)
test_grid.set_tile(0, 3, 2)
test_grid.set_tile(1, 0, 0)
test_grid.set_tile(1, 1, 0)
test_grid.set_tile(1, 2, 2)
test_grid.set_tile(1, 3, 8)
test_grid.set_tile(2, 0, 4)
test_grid.set_tile(2, 1, 2)
test_grid.set_tile(2, 2, 2)
test_grid.set_tile(2, 3, 8)
test_grid.set_tile(3, 0, 0)
test_grid.set_tile(3, 1, 2)
test_grid.set_tile(3, 2, 0)
test_grid.set_tile(3, 3, 4)

print test_grid

test_grid.move(UP)

print test_grid
#
# test_grid.move(RIGHT)
#
# print test_grid
#
# test_grid.move(RIGHT)
#
# print test_grid


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
