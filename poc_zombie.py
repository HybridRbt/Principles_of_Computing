"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
# import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        # clear obstacle
        poc_grid.Grid.clear(self)

        # clear human and zombie list
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for each_zombie in self._zombie_list:
            yield each_zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for each_human in self._human_list:
            yield each_human

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        # create a new grid "visited" of the same size as the original gird, inied as empty
        visited = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())

        # create distance_field and inied with max distance
        max_distance = self._grid_height * self._grid_width
        distance_field = [[max_distance for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]

        # create queue boundary
        boundary = poc_queue.Queue()

        if entity_type == "zombie":
            # copy zombie list
            for each_zombie in self._zombie_list:
                boundary.enqueue(each_zombie)
            # ini visited with the zombie list
            for each_zombie in self._zombie_list:
                visited.set_full(each_zombie[0], each_zombie[1])
                distance_field[each_zombie[0]][each_zombie[1]] = 0
        else:
            # copy human list
            for each_human in self._human_list:
                boundary.enqueue(each_human)
            # ini visited with the zombie list
            for each_human in self._human_list:
                visited.set_full(each_human[0], each_human[1])
                distance_field[each_human[0]][each_human[1]] = 0

        # do BFS search
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            for each_neighbor in self.four_neighbors(current_cell[0], current_cell[1]):
                if self.is_empty(each_neighbor[0], each_neighbor[1]) and visited.is_empty(each_neighbor[0],
                                                                                          each_neighbor[1]):
                    # not visited and passable
                    visited.set_full(each_neighbor[0], each_neighbor[1])
                    boundary.enqueue(each_neighbor)
                    # update distance
                    current_distance = distance_field[current_cell[0]][current_cell[1]]
                    distance_field[each_neighbor[0]][each_neighbor[1]] = current_distance + 1

        return distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for each_human in self.humans():
            # ini current pos to be the pos of this human
            current_pos = each_human
            current_distance = zombie_distance[each_human[0]][each_human[1]]
            # pick from 8 neighbors
            for each_neighbor in self.eight_neighbors(each_human[0], each_human[1]):
                if zombie_distance[each_neighbor[0]][each_neighbor[1]] > current_distance:
                    # better place, renew current distance
                    current_distance = zombie_distance[each_neighbor[0]][each_neighbor[1]]
                    current_pos = each_neighbor
                    # else stay
            # move human to the better place
            if current_pos != each_human:
                self.add_human(current_pos[0], current_pos[1])
                self._human_list.remove(each_human)

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for each_zombie in self.zombies():
            # ini current pos to be the pos of this zombie
            current_pos = each_zombie
            current_distance = human_distance[each_zombie[0]][each_zombie[1]]
            # pick from 4 neighbors
            for each_neighbor in self.four_neighbors(each_zombie[0], each_zombie[1]):
                if human_distance[each_neighbor[0]][each_neighbor[1]] < current_distance:
                    # better place, renew current distance
                    current_distance = human_distance[each_neighbor[0]][each_neighbor[1]]
                    current_pos = each_neighbor
                    # else stay
            # if it's not the same pos, move zombie to the better place
            if current_pos != each_zombie:
                self.add_zombie(current_pos[0], current_pos[1])
                self._zombie_list.remove(each_zombie)

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Zombie(30, 40))

# new_grid = Zombie(30, 30, [], [], [(2, 2)])
# print new_grid.compute_distance_field('human')
# # expected
# # [[4, 3, 2],
# #  [3, 2, 1],
# #  [2, 1, 0]]
