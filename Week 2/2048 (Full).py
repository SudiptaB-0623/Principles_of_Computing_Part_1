"""
Second week mini-project for Coursera Principles of Computing
Jari Leppanen 2015
Clone of 2048 game.
"""

#URL = #user40_ehG8nla8xBAntsP.py

#import poc_2048_gui
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
    length = len(line)
    merge_line = [element for element in line if element != 0]
    
    for index in range(0, len(merge_line)-1):
        if merge_line[index] == merge_line[index+1]:
            merge_line[index] *= 2
            merge_line[index+1] = 0
    merge_line = [element for element in merge_line if element != 0]
    while len(merge_line) != length:
        merge_line.append(0)
    
    return merge_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        
        up_indices = []
        for itr in range(grid_width):
            up_indices.append((0,itr))
            
        itr = 0
        down_indices = []
        for itr in range(grid_width):
            down_indices.append((grid_height-1,itr))
            
        itr = 0
        left_indices = []
        for itr in range(grid_height):
            left_indices.append((itr,0))
            
        itr = 0
        right_indices = []
        for itr in range(grid_height):
            right_indices.append((itr,grid_width-1))
            
        self._indices = {UP: up_indices,
                         DOWN: down_indices,
                         LEFT: left_indices,
                         RIGHT: right_indices}
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)]
                           for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = "["
        for row in range(self._height):
            grid_str += " " + str(self._grid[row]) + "\n"
        grid_str = grid_str[0:1] + grid_str[2:]
        grid_str = grid_str[:-1]
        grid_str += "]"
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        no_change = True
        if direction == UP or direction == DOWN:
            other_direction = self.get_grid_height()
        elif direction == LEFT or direction == RIGHT:
            other_direction = self.get_grid_width()
        for first_index in self._indices[direction]:
            row = first_index[0]
            col = first_index[1]
            line = []
            for _ in range(other_direction):
                line.append(self.get_tile(row, col))
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
            merged_line = merge(line)
            
            if merged_line != line:
                no_change = False
            
            row = first_index[0]
            col = first_index[1]
            for idx in range(other_direction):
                self.set_tile(row, col, merged_line[idx])
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
        if no_change == False: 
            self.new_tile()
                    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        two_or_four = random.random();
        if two_or_four < 0.9:
            value = 2
        else:
            value = 4
        empty = False
        all_cells = 0
        while empty == False:
            all_cells += 1 
            row = random.choice(range(self._height))
            col = random.choice(range(self._width))
            if self.get_tile(row, col) == 0:
                empty = True
                self.set_tile(row, col, value)
            elif all_cells >= self._height * self._width:
                empty = True

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value; 
            
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]
