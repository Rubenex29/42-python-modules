import sys
import random
from mlx import Mlx


class ImgData:
    """Structure for image data"""
    def __init__(self):
        self.img = None
        self.width = 0
        self.height = 0
        self.data = None
        self.sl = 0  # size line
        self.bpp = 0  # bits per pixel
        self.iformat = 0


class XVar:
    """Structure for main vars"""
    def __init__(self):
        self.mlx = None
        self.mlx_ptr = None
        self.screen_w = 0
        self.screen_h = 0
        self.win = None
        self.imgidx = 0
        self.default_maze = None

    def get_screen_sizes(self):
        """
        gets window size, might be handy in the future to have the window perfectly fit window and retroactively scale to maze_size-win_size
        """
        return self.win

    def set_maze(self, mazeing):
        """
        sets the default_maze value for later use within xvar stuff
        """
        self.default_maze = mazeing

    def get_default_maze(self):
        return self.default_maze


def draw_north_wall(xvar, coord_x, coord_y, size, color):
    edge = int(size * 0.07)
    for y in range(edge):
        for x in range(size):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_west_wall(xvar, coord_x, coord_y, size, color):
    edge = int(size * 0.07)
    for y in range(size):
        for x in range(edge):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_east_wall(xvar, coord_x, coord_y, size, color):
    edge = int(size * 0.07)
    for y in range(size):
        for x in range(size-edge, size):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_south_wall(xvar, coord_x, coord_y, size, color):
    edge = int(size * 0.07)
    for y in range(size-edge, size):
        for x in range(size):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_fourty_two(xvar, coord_x, coord_y, size, color):
    for y in range(size):
        for x in range(size):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_enter(xvar, coord_x, coord_y, size, color):
    """
    entry and path
    """
    margin = int(size * 0.11)
    # i want to change it to work with lines, not dots
    for y in range(int(size/2)-margin, int(size/2)+margin):
        for x in range(int(size/2)-margin, int(size/2)+margin):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def draw_end(xvar, coord_x, coord_y, size, color):
    margin = int(size * 0.11)
    for y in range(int(size/2)-margin, int(size/2)+margin):
        for x in range(int(size/2)-margin, int(size/2)+margin):
            xvar.mlx.mlx_pixel_put(xvar.mlx_ptr, xvar.win, x+coord_x*size, y+coord_y*size, color)


def gere_key(key, xvar):
    if key == 49:
        lol = MazeGenerator(WIDTH * HEIGHT, WIDTH, HEIGHT, BLOCK_SIZE, ENTRY, EXIT)
        xvar.set_maze(lol)
        lol.maze_carver(ENTRY[0], ENTRY[1])
        xvar.mlx.mlx_clear_window(xvar.mlx_ptr, xvar.win)
        with open(OUTPUT_FILE, "w") as output_file:
            output_file.write(xvar.get_default_maze().printMaze())
            output_file.write(xvar.get_default_maze().print_default_path(True))
        xvar.get_default_maze().printMlx(xvar)
        return 0

    if key == 50:
        xvar.mlx.mlx_clear_window(xvar.mlx_ptr, xvar.win)
        xvar.get_default_maze().toggle_solution_visible()
        xvar.get_default_maze().printMlx(xvar)
        return 0

    if key == 51:
        xvar.get_default_maze().next_color()
        xvar.mlx.mlx_clear_window(xvar.mlx_ptr, xvar.win)
        xvar.get_default_maze().printMlx(xvar)
        return 0

    if key == 52 or key == 65307:
        win_close(xvar)
        return 0


class Solver(object):
    """
    BUSTED SOLVER CLASS THAT I NEED TO FIX
    """
    def __init__(self, maze):
        self.path = []
        self.maze = {
            k: {kk: (False if vv is True and kk == "visited" else vv) for kk, vv in v.items()}
            for k, v in maze.items()
        }

    def solve(self, ENTRY, EXIT):
        """
        docstring
        """
        [x, y] = ENTRY
        while [x, y] != EXIT:
            print(x, y)
            if self.maze[(x, y)]["west"] == 0 and self.maze[(x, y)]["visited"] == False:
                print("west")
                x -= 1
                self.path.append((x, y))
            if self.maze[(x, y)]["east"] == 0 and self.maze[(x, y)]["visited"] == False:
                print("east")
                x += 1
                self.path.append((x, y))
            if self.maze[(x, y)]["south"] == 0 and self.maze[(x, y)]["visited"] == False:
                print("south")
                y += 1
                self.path.append((x, y))
            if self.maze[(x, y)]["north"] == 0 and self.maze[(x, y)]["visited"] == False:
                print("north")
                y -= 1
                self.path.append((x, y))
            print(x, y)
        return self.path


class MazeGenerator(object):  # this need to be in a standalone module
    """
    Maze generator with a built-in depth-first algorithm
    """
    def __init__(self, size, WIDTH, HEIGHT, BLOCK_SIZE, ENTRY, EXIT, SEED=0):
        self.size = size
        self.SEED = SEED
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.ENTRY = ENTRY
        self.EXIT = EXIT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.solution_visible = False
        self.visit_count = 0
        self.default_path = []
        self.maze = {}
        self.hasVisited = []
        self.two = [(1, 0), (2, 0), (3, 0), (3, -1), (3, -2), (2, -2), (1, -2), (1, 1), (1, 2), (2, 2), (3, 2)]
        self.four = [(-1, 0), (-2, 0), (-3, 0), (-3, -1), (-3, -2), (-1, 1), (-1, 2)]
        self.colors = [[0xFF1C73FF, 0xFFFF1CE5, 0xFFFFA81C, 0xFF1CFF36], [0xFF1CF0FF, 0xFF9D1CFF, 0xFFFF2B1C, 0xFF7EFF1C], [0xFFFF1C1C, 0xFF8EFF1C, 0xFF1CFFFF, 0xFF8E1CFF], [0xFFFF1CAC, 0xFFFFE11C, 0xFF1CFF6F, 0xFF1C3AFF]]
        self.curr_color = 0
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.maze[(x, y)] = {"west": 1, "south": 1, "east": 1, "north": 1, "visited": False, "42": False}
                if [x, y] == self.ENTRY:
                    self.maze[(x, y)]["visited"] = True
        self.fourty_two()

    def toggle_solution_visible(self):
        if self.solution_visible is True:
            self.solution_visible = False
        else:
            self.solution_visible = True

    def next_color(self):
        """
        Changes color to next
        """
        self.curr_color += 1
        if self.curr_color >= len(self.colors):
            self.curr_color = 0

    def fourty_two(self):
        two_x = int(self.WIDTH/2)
        four_x = int(self.WIDTH/2)
        y = int(self.HEIGHT/2)
        if self.WIDTH % 2 == 0:
            # two_x += 1
            four_x -= 1
        for two_coords in self.two:
            self.maze[(two_x + two_coords[0], y + two_coords[1])]["42"] = True
        for four_coords in self.four:
            self.maze[(four_x + four_coords[0], y + four_coords[1])]["42"] = True

    def bit_math(self, x, y) -> str:
        """
        This method will take the bits on the maze and math out what hex value it should be
        """
        hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        result = self.maze[(x, y)]["west"] * 2 * 2 * 2
        result += self.maze[(x, y)]["south"] * 2 * 2
        result += self.maze[(x, y)]["east"] * 2
        result += self.maze[(x, y)]["north"]
        return hex[result]

    def reverse_bit_math(self):  # take this out of this class and have it just be a helper function
        """
        Takes an hex and splits its parts into the corresponding maze wall bits,
        also takes care of entry, exit, and solution
        """
        x_coord = 0
        y_coord = 0
        ending_entries = 0
        prev = ""
        n = 0
        with open("maze.txt", "r") as file:
            for y in file:
                for x in y:
                    if prev == "\n" and x == "\n":
                        break
                    if x != "\n":
                        hex = int(x, 16)
                        maze = self.maze[(x_coord, y_coord)]
                        maze["west"] = int((hex/8) % 2)
                        maze["south"] = int((hex/4) % 2)
                        maze["east"] = int((hex/2) % 2)
                        maze["north"] = hex % 2
                        maze["visited"] = True
                    if x == "\n":
                        self.WIDTH = x_coord
                        x_coord = 0
                    else:
                        x_coord += 1
                    prev = x
                else:
                    if x == "\n":
                        y_coord += 1
                    continue
                self.HEIGHT = y_coord
                break
            for line in file:
                try:
                    thing = line.split()
                except Exception as e:
                    print(e)
                if ending_entries == 0:
                    ending_entries += 1
                    hold = thing[0].split(",")
                    self.ENTRY = [int(hold[0]), int(hold[1])]
                    continue
                if ending_entries == 1:
                    ending_entries += 1
                    hold = thing[0].split(",")
                    self.EXIT = [int(hold[0]), int(hold[1])]
                    continue
                if ending_entries == 2:
                    path = self.default_path
                    path.append(self.ENTRY)
                    for direction in thing[0]:
                        n += 1
                        if direction == "N":
                            path.append((path[n-1][0], path[n-1][1]-1))
                        if direction == "S":
                            path.append((path[n-1][0], path[n-1][1]+1))
                        if direction == "E":
                            path.append((path[n-1][0]+1, path[n-1][1]))
                        if direction == "W":
                            path.append((path[n-1][0]-1, path[n-1][1]))
                    path.pop()

    def printMaze(self):
        """Displays the maze data structure in the maze argument. The
        markX and markY arguments are coordinates of the current
        '@' location of the algorithm as it generates the maze."""
        result = ""
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(self.bit_math(x, y), end='')
                result += self.bit_math(x, y)
            print()
            result += "\n"
        print()
        result += "\n"
        print(f"{self.ENTRY[0]},{self.ENTRY[1]}")
        result += f"{self.ENTRY[0]},{self.ENTRY[1]}\n"
        print(f"{self.EXIT[0]},{self.EXIT[1]}")
        result += f"{self.EXIT[0]},{self.EXIT[1]}\n"
        return result

    def printMlx(self, xvar):
        """
        displays the maze using MLX on screen
        """
        size = self.BLOCK_SIZE  # THIS NEEDS TO CHANGE RETROACTIVELY WITH win SIZE
        color = self.colors[self.curr_color]
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.maze[(x, y)]["north"] == 1:
                    draw_north_wall(xvar, x, y, size, color[0])
                if self.maze[(x, y)]["south"] == 1:
                    draw_south_wall(xvar, x, y, size, color[0])
                if self.maze[(x, y)]["east"] == 1:
                    draw_east_wall(xvar, x, y, size, color[0])
                if self.maze[(x, y)]["west"] == 1:
                    draw_west_wall(xvar, x, y, size, color[0])
                if [x, y] == self.ENTRY:
                    draw_enter(xvar, x, y, size, color[3])
                if [x, y] == self.EXIT:
                    draw_end(xvar, x, y, size, color[1])
                if self.maze[(x, y)]["42"] is True:
                    draw_fourty_two(xvar, x, y, size, color[2])
                if self.solution_visible:
                    if (x, y) in self.default_path:
                        draw_path_line(xvar, x, y, size, color[3], "C")
                        path_index = self.default_path.index((x, y))
                        if path_index - 1 >= 0:
                            prev_x, prev_y = self.default_path[path_index - 1]
                            if prev_x > x:
                                draw_path_line(xvar, x, y, size, color[3], "E")
                            elif prev_x < x:
                                draw_path_line(xvar, x, y, size, color[3], "W")
                            elif prev_y > y:
                                draw_path_line(xvar, x, y, size, color[3], "S")
                            elif prev_y < y:
                                draw_path_line(xvar, x, y, size, color[3], "N")
                        if path_index + 1 < len(self.default_path):
                            next_x, next_y = self.default_path[path_index + 1]
                            if next_x > x:
                                draw_path_line(xvar, x, y, size, color[3], "E")
                            elif next_x < x:
                                draw_path_line(xvar, x, y, size, color[3], "W")
                            elif next_y > y:
                                draw_path_line(xvar, x, y, size, color[3], "S")
                            elif next_y < y:
                                draw_path_line(xvar, x, y, size, color[3], "N")
        xvar.mlx.mlx_string_put(xvar.mlx_ptr, xvar.win, 0, self.HEIGHT*size+10, color[0], "1: regen; 2: path; 3: color; 4: quit")

    def find_neighbours(self, x, y) -> list:  # this does not care if the cell has been visited or not, its up to the program that uses this to keep track of what it has seen
        """
        Finds valid neighbours of the cell at [x, y] and returns a dict with [(x, y), wall]
        """
        result = []

        def validator(self, new_x, new_y, demolished_wall):
            if new_x >= 0 and new_y >= 0 and new_x < self.WIDTH and new_y < self.HEIGHT:
                try:
                    new = self.maze[(new_x, new_y)]
                    if new["visited"] is False and new["42"] is False:
                        result.append([(new_x, new_y), demolished_wall])
                except Exception as e:
                    print("forsen", e)

        validator(self, x+1, y, "ew")
        validator(self, x, y+1, "sn")
        validator(self, x-1, y, "we")
        validator(self, x, y-1, "ns")

        if len(result):
            return result
        else:
            return None

    def maze_carver(self, x, y):  # depth-first
        """
        Carves the 'wall only' maze into a real maze
        """
        ended = False
        while self.visit_count < self.size:
            next_possible_cell = self.find_neighbours(x, y)
            if [x, y] == self.EXIT:
                ended = True
            if next_possible_cell is not None:
                self.hasVisited.append((x, y))
                if ended is False:
                    self.default_path.append((x, y))
                [(next_x, next_y), wall] = random.choice(next_possible_cell)
                if wall.startswith("s"):
                    self.maze[(x, y)]["south"] = 0
                    self.maze[(next_x, next_y)]["north"] = 0
                elif wall.startswith("n"):
                    self.maze[(x, y)]["north"] = 0
                    self.maze[(next_x, next_y)]["south"] = 0
                elif wall.startswith("e"):
                    self.maze[(x, y)]["east"] = 0
                    self.maze[(next_x, next_y)]["west"] = 0
                elif wall.startswith("w"):
                    self.maze[(x, y)]["west"] = 0
                    self.maze[(next_x, next_y)]["east"] = 0
                self.maze[(next_x, next_y)]["visited"] = True
                x = next_x
                y = next_y
                self.visit_count += 1
            elif len(self.hasVisited) > 0:
                (x, y) = self.hasVisited.pop()
                if ended is False:
                    (x, y) = self.default_path.pop()
            elif next_possible_cell is None and len(self.hasVisited) == 0:
                return

    def get_maze(self):
        """
        returns the working maze
        """
        return self.maze

    def print_default_path(self, instructions=False):
        """
        prints the default path calculated to solve the maze
        """
        result = ""
        if instructions is True:
            coords = self.default_path
            for n in range(len(coords)):
                try:
                    if coords[n][0]-coords[n+1][0] == 1:
                        print("W", end="")
                        result += "W"
                    if coords[n][0]-coords[n+1][0] == -1:
                        print("E", end="")
                        result += "E"
                    if coords[n][1]-coords[n+1][1] == 1:
                        print("N", end="")
                        result += "N"
                    if coords[n][1]-coords[n+1][1] == -1:
                        print("S", end="")
                        result += "S"
                except Exception:
                    if coords[n][0]-self.EXIT[0] == 1:
                        print("W")
                        result += "W"
                    if coords[n][0]-self.EXIT[0] == -1:
                        print("E")
                        result += "E"
                    if coords[n][1]-self.EXIT[1] == 1:
                        print("N")
                        result += "N"
                    if coords[n][1]-self.EXIT[1] == -1:
                        print("S")
                        result += "S"
        else:
            print(self.default_path)
        return result


def win_close(xvar):
    xvar.mlx.mlx_loop_exit(xvar.mlx_ptr)


if __name__ == "__main__":
    seeded = False
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                name, value = line.split("=")
                if name == "WIDTH":
                    WIDTH = int(value)
                if name == "HEIGHT":
                    HEIGHT = int(value)
                if name == "ENTRY":
                    x, y = value.split(",")
                    ENTRY = [int(x), int(y)]
                if name == "EXIT":
                    x, y = value.split(",")
                    EXIT = [int(x), int(y)]
                if name == "BLOCK_SIZE":
                    BLOCK_SIZE = int(value)
                if name == "OUTPUT_FILE":
                    OUTPUT_FILE = str(value).removesuffix("\n")
                if name == "PERFECT":
                    PERFECT = bool(value)
                if name == "SEED":
                    print("=== Seeded mode ===")
                    seeded = True
                    SEED = str(value)
                    print("WIDTH: ", WIDTH)
                    print("HEIGHT: ", HEIGHT)
                    print("BLOCK_SIZE: ", BLOCK_SIZE)
                    print("ENTRY: ", ENTRY)
                    print("EXIT: ", EXIT)
                    lol = MazeGenerator(WIDTH * HEIGHT, WIDTH, HEIGHT, BLOCK_SIZE, ENTRY, EXIT, SEED)
                    lol.reverse_bit_math()  # this must come BEFORE the MazeGenerator class and feed it its values
            if seeded is False:
                print("=== Random mode ===")
                lol = MazeGenerator(WIDTH * HEIGHT, WIDTH, HEIGHT, BLOCK_SIZE, ENTRY, EXIT)
                print("WIDTH: ", WIDTH)
                print("HEIGHT: ", HEIGHT)
                print("BLOCK_SIZE: ", BLOCK_SIZE)
                print("ENTRY: ", ENTRY)
                print("EXIT: ", EXIT)
                lol.maze_carver(ENTRY[0], ENTRY[1])
    except Exception as e:
        print(f"Some error happened on: {e}\nLoading maze with default values...\n")
        WIDTH = 30
        HEIGHT = 30
        ENTRY = [0, 0]
        EXIT = [WIDTH - 1, HEIGHT - 1]
        BLOCK_SIZE = 32
        OUTPUT_FILE = "maze.txt"
        # PERFECT = True
        # ^THIS IS THE DEFAULT!!! a very simple way of making an "imperfect" maze given our code is to simply erase BOTH east and south walls on [0, 0] and by definition it will be correct
        lol = MazeGenerator(WIDTH * HEIGHT, WIDTH, HEIGHT, BLOCK_SIZE, ENTRY, EXIT)
        lol.maze_carver(ENTRY[0], ENTRY[1])

    # vvvv THIS CHECKER MUST HAPPEN INSIDE THE PREV BLOCKS ^^^^^
    if WIDTH <= 8:
        WIDTH = 9
    if HEIGHT <= 6:
        HEIGHT = 7
    if EXIT[0] >= WIDTH:
        EXIT[0] = ENTRY[0]+1
    if EXIT[1] >= HEIGHT:
        EXIT[1] = ENTRY[1]+1
    # TODO we need an override for invalid exits inside ENTRY or within 42
    # ^ possibly put this fail safe on the fourty_two method in the big maze class

    xvar = XVar()
    # Mlx Initialisation
    try:
        xvar.mlx = Mlx()
    except Exception as e:
        print(f"Error: Can't initialize MLX: {e}", file=sys.stderr)
        sys.exit(1)

    xvar.mlx_ptr = xvar.mlx.mlx_init()

    ret, xvar.screen_w, xvar.screen_h = xvar.mlx.mlx_get_screen_size(xvar.mlx_ptr)

    # Windows creation
    try:
        xvar.win = xvar.mlx.mlx_new_window(xvar.mlx_ptr, BLOCK_SIZE*WIDTH, BLOCK_SIZE*HEIGHT + 40, "MLX main win")  # infer size from HEIGHT and WIDTH | THE EXTRA height is for options
        if not xvar.win:
            raise Exception("Can't create main window")
    except Exception as e:
        print(f"Error Win create: {e}", file=sys.stderr)
        sys.exit(1)

    xvar.set_maze(lol)

    mlx = Mlx()
    mlx.mlx_init()
    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write(lol.printMaze())
        output_file.write(lol.print_default_path(True))
    lol.printMlx(xvar)
    # solved = Solver(lol.get_maze())
    # solved.solve(ENTRY, EXIT)
    # ^these do not work, if we implement some other solver, it will probably work like this tho

    xvar.mlx.mlx_key_hook(xvar.win, gere_key, xvar)
    xvar.mlx.mlx_hook(xvar.win, 33, 0, win_close, xvar)
    xvar.mlx.mlx_loop(xvar.mlx_ptr)

    # Cleaning resources
    print("destroy win")
    xvar.mlx.mlx_destroy_window(xvar.mlx_ptr, xvar.win)
    print("destroy mlx")
    xvar.mlx.mlx_release(xvar.mlx_ptr)


# TODO
# Optional: set specific colours to display the “42” pattern.
# ^literally free, just a matter of splitting the pallet of the 42

# TODO Xtone special
# BLOCK_SIZE should be a value so that either the display fills the monitor VERTICALLY or HORIZONTALLY
# ^if vertically, i need to take the few extra pixels for the keybinds into account

# line solution
# ^i am quite unsure how i would go about this, maybe just offset a wedge...

# TODO BONUS
# Support multiple maze generation algorithms
# ^simple enough

# Add animation during maze generation
# ^split the printing maze from printing the solution, then stagger the solution

# TODO EXTRA
# README.md
