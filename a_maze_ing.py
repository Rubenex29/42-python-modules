# import sys
import random


class MazeGenerator(object):  # this need to be in a standalone module
    """
    docstring
    """
    def __init__(self, size, seed, WIDTH, HEIGHT, WALL):
        self.size = size
        self.seed = seed
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WALL = WALL
        self.maze = {}
        self.hasVisited = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.maze[(x, y)] = WALL

    def printMaze(self, ENTRY, EXIT):
        """Displays the maze data structure in the maze argument. The
        markX and markY arguments are coordinates of the current
        '@' location of the algorithm as it generates the maze."""
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if [x, y] == ENTRY:
                    print(MARK, end='')
                elif [x, y] == EXIT:
                    print(END, end='')
                elif x+1 == WIDTH or y+1 == HEIGHT:
                    print(WALL, end='')
                else:
                    print(self.maze[(x, y)], end='')
            print()

    def find_neighbours(self, x, y) -> list:  # this does not care if the cell has been visited or not, its up to the program that uses this to keep track of what it has seen
        """
        Finds valid neighbours of the cell at [x, y] and returns a list
        """
        result = []

        def validator(new_x, new_y):
            if new_x > 0 and new_y > 0 and new_x < self.HEIGHT and new_y < self.WIDTH:
                result.append((new_x, new_y))

        validator(x+1, y)
        validator(x, y+1)
        validator(x-1, y)
        validator(x, y-1)

        if len(result):
            return result
        else:
            return None

    def maze_carver(self, x, y):
        """
        Carves the 'wall only' maze into a real maze
        """
        pass

    def visit(self, x, y):
        """"Carve out" empty spaces in the maze at x, y and then
        recursively move to neighboring unvisited spaces. This
        function backtracks when the mark has reached a dead end."""
        self.maze[(x, y)] = EMPTY  # "Carve out" the space at x, y.
        self.printMaze(x, y)  # Display the maze as we generate it.
        # print('\n\n')
        print(self.maze)
        while True:
            # Check which neighboring spaces adjacent to
            # the mark have not been visited already:
            unvisitedNeighbors = []
            if y > 1 and (x, y - 2) not in self.hasVisited:
                unvisitedNeighbors.append(NORTH)

            if y < HEIGHT - 2 and (x, y + 2) not in self.hasVisited:
                unvisitedNeighbors.append(SOUTH)

            if x > 1 and (x - 2, y) not in self.hasVisited:
                unvisitedNeighbors.append(WEST)

            if x < WIDTH - 2 and (x + 2, y) not in self.hasVisited:
                unvisitedNeighbors.append(EAST)

            if len(unvisitedNeighbors) == 0:
                # BASE CASE
                # All neighboring spaces have been visited, so this is a
                # dead end. Backtrack to an earlier space:
                return
            else:
                # RECURSIVE CASE
                # Randomly pick an unvisited neighbor to visit:
                nextIntersection = random.choice(unvisitedNeighbors)

                # Move the mark to an unvisited neighboring space:

                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    self.maze[(x, y - 1)] = EMPTY  # Connecting hallway.
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    self.maze[(x, y + 1)] = EMPTY  # Connecting hallway.
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    self.maze[(x - 1, y)] = EMPTY  # Connecting hallway.
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    self.maze[(x + 1, y)] = EMPTY  # Connecting hallway.

                self.hasVisited.append((nextX, nextY))  # Mark as visited.
                self.visit(nextX, nextY)  # Recursively visit this space.

    # # Carve out the paths in the maze data structure:
    # hasVisited = [(1, 1)]  # Start by visiting the top-left corner.
    # visit(1, 1)

    # # Display the final resulting maze data structure:
    # printMaze(maze)


if __name__ == "__main__":
    WIDTH = 10
    HEIGHT = 10
    ENTRY = [2, 2]
    EXIT = [WIDTH - 2, HEIGHT - 2]
    OUTPUT_FILE = "maze.txt"
    SEED = 1  # new
    # PERFECT=True  # needed
    EMPTY = " "
    MARK = '@'
    END = "E"
    WALL = chr(9608)
    NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'
    lol = MazeGenerator(1, 1, WIDTH, HEIGHT, WALL)
    # lol.printMaze()
    # lol.visit(1, 1)  # prob need to make this the ENTRY point
    print(lol.find_neighbours(2, 2))
    print()
    lol.printMaze(ENTRY, EXIT)
