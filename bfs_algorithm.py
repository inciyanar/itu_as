from collections import deque

class Map: #list of the map
    def __init__(self, grid: list[list[int]]):
        self.height: int = 8
        self.weight: int = 8
        self.grid = grid #the grid keeps by list of the list of the cells.
        self.entry = (0, 0)
        self.exit = (7, 7)
        self.map_borders = []

    def neighbor_checker(self, cell_coord: tuple[int, int]) -> list[tuple[int, int]]: #checks if there is a way around the cell
        row, col= cell_coord
        open_neighbors: list[tuple[int, int]] = [] #ways that a cell can move to

        if row - 1 >= 0 and self.grid[row -1][col] == 0: # when moving to the north side, row = row - 1. first check if its out of boundires, then check if there is any barrier.
            open_neighbors.append((row - 1, col)) # if it is safe, submit as a moveable cell.
        if col + 1 < self.width and self.grid[row][col + 1] == 0: # east
            open_neighbors.append((row, col + 1))
        if row + 1 < self.height and self.grid[row + 1][col] == 0: # south
            open_neighbors.append((row + 1, col))
        if col - 1 >= 0 and self.grid[row][col - 1] == 0:
            open_neighbors.append((row, col - 1))
        return (open_neighbors)


    def find_solution(self) -> list[list[tuple[int, int]]]: #finds more than one solution, in terms of anything happen to the shorthest way the other solution ways are ready.
        start = self.entry
        end = self.exit
        queue = deque([([start], {start})]) #keeps the line
        paths = list[list[list[tuple[int , int]]]] = []



if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
            ]
    our_map = map(grid)
