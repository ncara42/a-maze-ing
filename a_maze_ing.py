import sys
import os
import random
from typing import Any


class Color:
    """
    A class containing some clors used during execution
    """
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    gray = "\033[90m"
    white = "\u001b[37m"
    reset = "\033[0m"


class Parameters:
    """
    The class thar contains all maze parameters that
    should be read with read_config
    """
    def __init__(self) -> None:
        self.width = -1
        self.height = -1
        self.entry = [-1, -1]
        self.exit = [-1, -1]
        self.output_filename = ""
        self.perfect = -1
        self.seed: int | None = 42
        self.seed_is_random: bool = True

    def printParams(self) -> None:
        """
        This function prints the parametrs that have previously been
        assigned.
        """
        print("Width:", self.width)
        print("Height:", self.height)
        print("Entry:", self.entry)
        print("Exit:", self.exit)
        print("Output:", self.output_filename)
        print("Perfect:", self.perfect)
        print("Seed:", self.seed)

    def correctParams(self) -> bool:
        """
        This function checks if the parametrs that have previously been
        assigned are correct for the program to continue.
        """
        errors = 0
        if self.width < 0:
            print(f"Argument not correct or present: {Color.red}"
                  f"WIDTH{Color.reset}.")
            print(f"Expected: WIDTH={Color.green}<INT>{Color.reset}")
            errors += 1
        if self.height < 0:
            print(f"Argument not correct or present: {Color.red}"
                  f"HEIGHT{Color.reset}.")
            print(f"Expected: HEIGHT={Color.green}<INT>{Color.reset}")
            errors += 1
        if self.entry[0] < 0 or self.entry[0] > self.width - 1 or \
           self.entry[1] < 0 or self.entry[1] > self.height - 1:
            print(f"Argument not correct or present: {Color.red}"
                  f"ENTRY{Color.reset}.")
            print(f"Expected: ENTRY={Color.green}<INT>, <INT>{Color.reset}")
            errors += 1
        if self.exit[0] < 0 or self.exit[0] > self.width - 1 or \
           self.exit[1] < 0 or self.exit[1] > self.height - 1:
            print(f"Argument not correct or present: {Color.red}"
                  f"EXIT{Color.reset}.")
            print(f"Expected: EXIT={Color.green}<INT>, <INT>{Color.reset}")
            errors += 1
        if not self.output_filename:
            print(f"Argument not correct or present: {Color.red}"
                  f"OUTPUT_FILE{Color.reset}.")
            print(f"Expected: OUTPUT_FILE={Color.green}<STRING>{Color.reset}")
            errors += 1
        if self.perfect < 0:
            print(f"Argument not correct or present: {Color.red}"
                  f"PERFECT{Color.reset}.")
            print(f"Expected: PERFECT={Color.green}<BOOLEAN>{Color.reset}")
            errors += 1
        if self.entry == self.exit:
            print(f"{Color.red}Error:{Color.reset} ENTRY and EXIT should be "
                  "different.")
            errors += 1
        if self.seed == 42:
            print(f"Optional argument not present: {Color.red}"
                  f"SEED{Color.reset}.")
            print(f"Expected: SEED={Color.green}<INT>{Color.reset}")
            print(f"{Color.blue}The seed was set to 42 by default"
                  f"{Color.reset}.")
        if errors == 0:
            return True
        return False

    @classmethod
    def read_config(cls, _file_name: str) -> Any:
        """
        Read _file_name and store  the data in a Parameters object

        :param _file_name: The name of the file to read.
        :type _file_name: str
        :return: The Parameters object or None if error
        :rtype: Parameters
        """
        parameters = Parameters()
        try:
            config = open(_file_name)
            line = []
            while (line := config.readline().strip().split('=')) != ['']:
                if len(line) == 2:
                    if line[0] == "WIDTH":
                        try:
                            parameters.width = int(line[1])
                        except ValueError:
                            print(f"Argument not correct: {Color.red}"
                                  f"WIDTH{Color.reset}.")
                            print(f"Expected: WIDTH={Color.green}<INT>"
                                  f"{Color.reset}")
                            return None
                    if line[0] == "HEIGHT":
                        try:
                            parameters.height = int(line[1])
                        except ValueError:
                            print(f"Argument not correct: {Color.red}"
                                  f"HEIGHT{Color.reset}.")
                            print(f"Expected: HEIGHT={Color.green}<INT>"
                                  f"{Color.reset}")
                            return None
                    if line[0] == "ENTRY":
                        try:
                            parameters.entry[0] = int(line[1].split(',')[0])
                            parameters.entry[1] = int(line[1].split(',')[1])
                        except ValueError:
                            print(f"Argument not correct: {Color.red}"
                                  f"ENTRY{Color.reset}.")
                            print(f"Expected: ENTRY={Color.green}<INT>, "
                                  f"<INT>{Color.reset}")
                            return None
                    if line[0] == "EXIT":
                        try:
                            parameters.exit[0] = int(line[1].split(',')[0])
                            parameters.exit[1] = int(line[1].split(',')[1])
                        except ValueError:
                            print(f"Argument not correct: {Color.red}"
                                  f"ENTRY{Color.reset}.")
                            print(f"Expected: ENTRY={Color.green}<INT>, "
                                  f"<INT>{Color.reset}")
                            return None
                    if line[0] == "OUTPUT_FILE":
                        parameters.output_filename = line[1]
                    if line[0] == "PERFECT":
                        if line[1] == "True":
                            parameters.perfect = True
                        elif line[1] == "False":
                            parameters.perfect = False
                        else:
                            print(f"Argument not correct: {Color.red}"
                                  f"PERFECT{Color.reset}.")
                            print(f"Expected: PERFECT={Color.green}<BOOLEAN>"
                                  f"{Color.reset}")
                            return None
                    if line[0] == "SEED":
                        try:
                            value = line[1].strip()
                            if value == "":
                                parameters.seed = random.randint(1, 9999)
                                parameters.seed_is_random = True
                            else:
                                parameters.seed = int(value)
                                parameters.seed_is_random = False

                        except ValueError:
                            print(f"Argument not correct: {Color.red}"
                                  f"SEED{Color.reset}.")
                            print(f"Expected: SEED={Color.green}<INT>"
                                  f"{Color.reset}")
                            return None
            config.close()
            if not parameters.correctParams():
                return None
        except FileNotFoundError:
            print(f"{Color.red}Error:{Color.reset}Configuration "
                  "file not found.")
            return None
        return parameters


class Cell:
    """
    A Cell class that has atributes: visited, walls: set, position: tuple
    """
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize the Cell object
        """
        self.visited = False
        self.walls = {"Top", "Right", "Bottom", "Left"}
        self.position = (x, y)

    def printCell(self, fileObject: Any) -> None:
        """
        Print the cell walls in hex format into file
        """
        base = "0123456789ABCDEF"
        toPrint = 0b0
        if "Left" in self.walls:
            toPrint += 1
        toPrint <<= 1
        if "Bottom" in self.walls:
            toPrint += 1
        toPrint <<= 1
        if "Right" in self.walls:
            toPrint += 1
        toPrint <<= 1
        if "Top" in self.walls:
            toPrint += 1
        print(base[toPrint], file=fileObject, end='')


class Maze:
    """
    Represents a maze composed of cells arranged in a grid.
    Provides functionality to generate, solve, export, and visualize the maze.
    """

    def __init__(self, params: Parameters):
        """
        Initialize the maze grid based on the given parameters.
        """
        self.grid = []
        self.midle = (int(params.height/2), int(params.width/2))
        self.params = params
        for y in range(0, params.height):
            row = []
            for x in range(0, params.width):
                row.append(Cell(x, y))
            self.grid.append(row)

    def ft_watermark(self) -> None:
        """
        Places a predefined watermark pattern at the center of the maze.
        The watermark is applied only if it does not intersect with
        the entry or exit points and the maze dimensions are large enough.
        """
        (h, w) = self.midle
        shape = [
            [1, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1]
        ]

        start_y = h - (len(shape) // 2)
        start_x = w - (len(shape[0]) // 2)

        temp_watermark = []

        for y_idx, row in enumerate(shape):
            for x_idx, val in enumerate(row):
                if val == 1:
                    temp_watermark.append((start_x + x_idx, start_y + y_idx))

        self.watermark = []

        if self.params.height > 10 and self.params.width > 12:
            ent = (int(self.params.entry[0]), int(self.params.entry[1]))
            sal = (int(self.params.exit[0]), int(self.params.exit[1]))
            entry_exit = {ent, sal}

            intersection = entry_exit.intersection(temp_watermark)

            if not intersection:
                self.watermark = temp_watermark
                for x, y in self.watermark:
                    self.grid[y][x].visited = True
            else:
                self.watermark = []

    def createMaze(self) -> None:
        """
        Generates the maze by removing walls between cells using
        a depth-first search backtracking algorithm.
        """

        def deleteWalls(currentCell: Cell, nextCell: Cell) -> None:
            """
            Removes the walls between two adjacent cells.
            """
            (xCurrent, yCurrent) = currentCell.position
            (xNext, yNext) = nextCell.position
            if xCurrent > xNext:
                if "Left" in currentCell.walls:
                    currentCell.walls.remove("Left")
                if "Right" in nextCell.walls:
                    nextCell.walls.remove("Right")
            elif xCurrent < xNext:
                if "Right" in currentCell.walls:
                    currentCell.walls.remove("Right")
                if "Left" in nextCell.walls:
                    nextCell.walls.remove("Left")
            elif yCurrent > yNext:
                if "Bottom" in nextCell.walls:
                    nextCell.walls.remove("Bottom")
                if "Top" in currentCell.walls:
                    currentCell.walls.remove("Top")
            elif yCurrent < yNext:
                if "Top" in nextCell.walls:
                    nextCell.walls.remove("Top")
                if "Bottom" in currentCell.walls:
                    currentCell.walls.remove("Bottom")

        def canContinueMoving(cellPos: tuple[int, int]) -> list[Cell]:
            """
            Returns a list of adjacent cells that have not been visited yet.

            :param cellPos: The position of the current cell.
            :return: A list of unvisited neighboring cells.
            """
            (x, y) = cellPos
            posibilities = []
            if y < self.params.height - 1 and not self.grid[y+1][x].visited:
                posibilities.append(self.grid[y+1][x])
            if y > 0 and not self.grid[y-1][x].visited:
                posibilities.append(self.grid[y-1][x])
            if x < self.params.width - 1 and not self.grid[y][x+1].visited:
                posibilities.append(self.grid[y][x+1])
            if x > 0 and not self.grid[y][x-1].visited:
                posibilities.append(self.grid[y][x-1])
            return posibilities

        def delete_random_walls(grid: list[Any],
                                width: int, height: int) -> None:
            """
            Randomly removes additional walls from the maze to create loops
            when the maze is not required to be perfect.
            """
            number_of_walls_to_remove: int = int(width*height * 0.15)
            while number_of_walls_to_remove != 0:
                row: list[Cell] = random.choice(grid)
                cell: Cell = random.choice(row)
                if len(cell.walls) < 4 and len(cell.walls) != 0:
                    (x, y) = cell.position
                    posibilities = []
                    if y < height - 1 and len(grid[y+1][x].walls) < 4:
                        posibilities.append(grid[y+1][x])
                    if y > 0 and len(grid[y-1][x].walls) < 4:
                        posibilities.append(grid[y-1][x])
                    if x < width - 1 and len(grid[y][x+1].walls) < 4:
                        posibilities.append(grid[y][x+1])
                    if x > 0 and len(grid[y][x-1].walls) < 4:
                        posibilities.append(grid[y][x-1])
                    if len(posibilities) != 0:
                        deleteWalls(cell, random.choice(posibilities))
                        number_of_walls_to_remove -= 1

        print("start maze creation")
        _visitedCells = []
        _currentCell = self.grid[self.params.entry[1]][self.params.entry[0]]
        _visitedCells.append(_currentCell)
        _currentCell.visited = True
        while _visitedCells:
            posibilities = canContinueMoving(_currentCell.position)
            if len(posibilities) != 0 \
               and _currentCell.position != tuple(self.params.exit):
                _nexCell = random.choice(posibilities)
                deleteWalls(_currentCell, _nexCell)
                _currentCell = _nexCell
                _currentCell.visited = True
                _visitedCells.append(_currentCell)
            else:
                _currentCell.visited = True
                _visitedCells.pop(-1)
                if _visitedCells:
                    _currentCell = _visitedCells[-1]

        if not self.params.perfect:
            delete_random_walls(self.grid, self.params.width,
                                self.params.height)

        print("end maze creation")

    def solve(self) -> list[tuple[int, int]]:
        """
        Solves the maze using breadth-first search (BFS)
        and returns the path from entry to exit.
        """
        start = tuple(self.params.entry)
        goal = tuple(self.params.exit)

        queue = [start]
        parent_map: dict[Any, Any] = {}
        parent_map[start] = None
        while queue:
            current = queue.pop(0)

            if current == goal:
                break

            x, y = current
            cell = self.grid[y][x]

            neighbors = [
                ((x, y - 1), "Top"),
                ((x + 1, y), "Right"),
                ((x, y + 1), "Bottom"),
                ((x - 1, y), "Left")
            ]

            for (nx, ny), wall in neighbors:
                if 0 <= nx < self.params.width \
                        and 0 <= ny < self.params.height:
                    if wall not in cell.walls and (nx, ny) not in parent_map:
                        parent_map[(nx, ny)] = current
                        queue.append((nx, ny))

        path = []
        step: Any = goal

        while step is not None:
            path.append(step)
            step = parent_map.get(step)

        self.solution: list[tuple[int, int]] = path[::-1]
        return self.solution

    def export(self, output: Any) -> None:
        """
        Exports the maze structure, entry/exit points,
        and solution path to the given output stream.
        """
        for row in self.grid:
            for cell in row:
                cell.printCell(output)
            print(file=output)

        print(file=output)
        (x, y) = (self.params.entry)
        print(f"{x}, {y}", file=output)
        (x, y) = (self.params.exit)
        print(f"{x}, {y}", file=output)
        solution: list[tuple[int, int]] = self.solve()
        previous: tuple[int, int] = solution[0]
        for (y, x) in solution:
            py, px = previous
            if px > x:
                print("N", end='', file=output)
            elif px < x:
                print("S", end='', file=output)
            elif py > y:
                print("W", end='', file=output)
            elif py < y:
                print("E", end='', file=output)
            previous = (y, x)
        print(file=output)

    def printMap(self, bool_solve: bool) -> None:
        """
        Prints a visual representation of the maze to the console.
        """
        if not hasattr(self, 'solution'):
            self.solution = []

        if bool_solve is True:
            draw_path = self.solution
        else:
            draw_path = []

        WALL = f"{Color.gray}██{Color.reset}"
        PATH = f"{Color.green}██{Color.reset}"
        START = f"{Color.red}██{Color.reset}"
        EXIT = f"{Color.blue}██{Color.reset}"
        MARK = f"{Color.blue}██{Color.reset}"
        EMPTY = "  "

        watermark_coords = getattr(self, 'watermark', [])

        for y in range(self.params.height):
            top_line = ""
            for x in range(self.params.width):
                top_line += WALL

                if "Top" not in self.grid[y][x].walls \
                        and (x, y) in draw_path \
                        and (x, y-1) in draw_path:
                    top_line += PATH
                else:
                    if "Top" in self.grid[y][x].walls:
                        top_line += WALL
                    else:
                        top_line += EMPTY
            print(top_line + WALL)

            mid_line = ""
            for x in range(self.params.width):
                if "Left" not in self.grid[y][x].walls \
                  and (x, y) in draw_path and (x-1, y) in draw_path:
                    mid_line += PATH
                else:
                    if "Left" in self.grid[y][x].walls:
                        mid_line += WALL
                    else:
                        mid_line += EMPTY

                pos = (x, y)
                if pos == tuple(self.params.entry):
                    mid_line += START
                elif pos == tuple(self.params.exit):
                    mid_line += EXIT
                elif pos in watermark_coords:
                    mid_line += MARK
                elif pos in draw_path:
                    mid_line += PATH
                else:
                    mid_line += EMPTY
            print(mid_line + WALL)

        print(WALL * (self.params.width * 2 + 1))


def clear() -> None:
    os.system('clear' if os.name == 'posix' else 'cls')


def main() -> None:
    """
    Controls the number of arguments received and executes
    the program in order, including the required
    menu controlled by options.
    """
    if len(sys.argv) == 1:
        print(f"{Color.red}Error:{Color.reset} Configuration file"
              " not specified, expected: a_maze_ing.py"
              f"{Color.green} <filename> {Color.reset}")
    elif len(sys.argv) != 2:
        print(f"{Color.red}Error:{Color.reset} Too many arguments for the "
              "program, expected: a_maze_ing.py"
              f"{Color.green} <filename> {Color.reset}")
    else:
        try:
            parameters = Parameters.read_config(sys.argv[1])
            if not parameters:
                return

            random.seed(parameters.seed)
            maze = Maze(parameters)
            maze.ft_watermark()

            if not maze.watermark:
                print(f"{Color.red}The exit or entrance collides with mark 42."
                      f" Choose other coordinates.")
                return

            maze.createMaze()

            with open(parameters.output_filename, mode="w+") as output:
                maze.export(output)
                output.close()

            bool_solve = False
            bool_color: int = 0
            color_list = ["\033[33m", "\033[35m", "\033[90m", "\u001b[37m"]
            o_solution = "Show solution"

            while True:
                clear()
                maze.printMap(bool_solve)

                print(f"\n{Color.white}=== A-Maze-ing ==={Color.reset} \n"
                      f"\nSeed: {Color.green}{maze.params.seed}{Color.reset}\n"
                      f"\n{Color.green}1{Color.reset} - {o_solution}"
                      f"\n{Color.green}2{Color.reset} - Change color "
                      "(between presets)"
                      f"\n{Color.green}3{Color.reset} - Regenerate"
                      f" \n{Color.green}4{Color.reset} - Exit")
                option = input("\nOption: ").lower()

                if option == '1':
                    if not hasattr(maze, 'solution') \
                            or len(maze.solution) == 0:
                        maze.solve()
                    if not bool_solve:
                        o_solution = "Hide solution"
                    else:
                        o_solution = "Show solution"
                    bool_solve = not bool_solve
                elif option == '2':
                    Color.gray = color_list[bool_color % len(color_list)]
                    bool_color += 1
                elif option == '3':
                    parameters.seed = random.randint(1, 9999)
                    random.seed(parameters.seed)

                    maze = Maze(parameters)
                    maze.ft_watermark()
                    maze.createMaze()

                    with open(parameters.output_filename, mode="w+") as output:
                        maze.export(output)

                    bool_solve = False
                    o_solution = "Show solution"
                elif option == '4':
                    break

        except Exception as e:
            print(f"Error {e}")


if (__name__ == "__main__"):
    main()
