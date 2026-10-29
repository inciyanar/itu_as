from collections import deque

class Cell: #defining the cells of the map, every cell has a x,y tuple. 0: water/ 1: barrier
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.coordinate = (x, y)
        self.barrier = {"NORTH": 0, "EAST": 0, "WEST": 0, "SOUTH": 0}
    def get_hex_value(self) -> str:
        return f"{self.barrier:X}"

class Map: #list of the map
    def __init__(self):
        self.height: int = 8
        self.weight: int = 8
        self.grid = list[list[Cell]] = [] #the grid keeps by list of the list of the cells.
        self.entry = (0, 0)
        self.exit = (7, 7)

    def find_solution(self) -> list[list[tuple[int, int]]]: #finds more than one solution, in terms of anything happen to the shorthest way the other solution ways are ready.
        start = self.entry
        end = self.exit
        queue = deque([([start], {start})]) #keeps the line
        paths = list[list[list[tuple[int , int]]]] = []



if __name__ == "__main__":
