"""mazegen: a small, reusable maze generator.

Quick start
-----------
>>> from mazegen import MazeGenerator
>>> gen = MazeGenerator(width=10, height=6, seed=42)
>>> gen.generate()
>>> gen.entry, gen.exit
((0, 0), (9, 5))
>>> len(gen.solution) > 0
True

Custom parameters
-----------------
- Size: pass `width` and `height`.
- Seed: pass `seed` for reproducible mazes.
- Entry/exit: pass `entry=(x, y)` and `exit=(x, y)`.

Accessing the maze structure and a solution
-------------------------------------------
- `gen.grid` is a dict keyed by `(x, y)`; each cell has `walls` and `visited`.
- `gen.solution` is a list of `(x, y)` from entry to exit.
- Use `gen.solve()` to compute a shortest path at any time.

This module is intentionally single-file so it can be packaged as a simple
`pyproject` with `py-modules = ["mazegen"]`.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import random

Coord = Tuple[int, int]


@dataclass
class Cell:
    walls: Dict[str, bool]
    visited: bool = False


class MazeGenerator:
    """Depth-first maze generator with optional BFS solver."""

    def __init__(
        self,
        width: int,
        height: int,
        seed: Optional[int] = None,
        entry: Optional[Coord] = None,
        exit: Optional[Coord] = None,
    ) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height
        self.seed = seed
        self.random = random.Random(seed)
        self.entry = entry if entry is not None else (0, 0)
        self.exit = exit if exit is not None else (width - 1, height - 1)
        self.grid: Dict[Coord, Cell] = {}
        self.solution: List[Coord] = []
        self._init_grid()

    def _init_grid(self) -> None:
        self.grid.clear()
        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x, y)] = Cell(
                    walls={"n": True, "s": True, "e": True, "w": True},
                    visited=False,
                )

    def generate(self) -> None:
        """Generate a maze using randomized depth-first search."""
        self._init_grid()
        start = self.entry
        stack: List[Coord] = [start]
        self.grid[start].visited = True

        while stack:
            current = stack[-1]
            neighbors = self._unvisited_neighbors(current)
            if not neighbors:
                stack.pop()
                continue
            next_cell, direction = self.random.choice(neighbors)
            self._knock_down_wall(current, next_cell, direction)
            self.grid[next_cell].visited = True
            stack.append(next_cell)

        self.solution = self.solve()

    def _unvisited_neighbors(self, coord: Coord) -> List[Tuple[Coord, str]]:
        x, y = coord
        candidates = [
            ((x, y - 1), "n"),
            ((x, y + 1), "s"),
            ((x + 1, y), "e"),
            ((x - 1, y), "w"),
        ]
        valid: List[Tuple[Coord, str]] = []
        for (nx, ny), direction in candidates:
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if not self.grid[(nx, ny)].visited:
                    valid.append(((nx, ny), direction))
        return valid

    def _knock_down_wall(self, current: Coord, nxt: Coord, direction: str) -> None:
        opposite = {"n": "s", "s": "n", "e": "w", "w": "e"}
        self.grid[current].walls[direction] = False
        self.grid[nxt].walls[opposite[direction]] = False

    def solve(self) -> List[Coord]:
        """Solve the maze with BFS; returns shortest path or empty list."""
        start, goal = self.entry, self.exit
        queue = deque([start])
        came_from: Dict[Coord, Optional[Coord]] = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor in self._open_neighbors(current):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

        if goal not in came_from:
            return []

        path: List[Coord] = []
        cur: Optional[Coord] = goal
        while cur is not None:
            path.append(cur)
            cur = came_from[cur]
        path.reverse()
        return path

    def _open_neighbors(self, coord: Coord) -> List[Coord]:
        x, y = coord
        cell = self.grid[coord]
        neighbors: List[Coord] = []
        if not cell.walls["n"]:
            neighbors.append((x, y - 1))
        if not cell.walls["s"]:
            neighbors.append((x, y + 1))
        if not cell.walls["e"]:
            neighbors.append((x + 1, y))
        if not cell.walls["w"]:
            neighbors.append((x - 1, y))
        return neighbors

    def to_hex_lines(self) -> List[str]:
        """Export maze walls as hex strings (one row per line)."""
        hex_map = "0123456789ABCDEF"
        lines: List[str] = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = self.grid[(x, y)]
                value = (
                    (8 if cell.walls["w"] else 0)
                    + (4 if cell.walls["s"] else 0)
                    + (2 if cell.walls["e"] else 0)
                    + (1 if cell.walls["n"] else 0)
                )
                row.append(hex_map[value])
            lines.append("".join(row))
        return lines


if __name__ == "__main__":
    generator = MazeGenerator(width=12, height=8, seed=7)
    generator.generate()
    print("Entry:", generator.entry)
    print("Exit:", generator.exit)
    print("Solution length:", len(generator.solution))
    for line in generator.to_hex_lines():
        print(line)
