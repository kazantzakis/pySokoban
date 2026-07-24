import copy
from pathlib import Path


class Level:

    def __init__(self, set_name, level_num):

        # Instance attributes: each Level object gets its own
        # matrix and undo history (not shared across instances)
        self.matrix = []
        self.matrix_history = []

        level_path = (Path(__file__).resolve().parent / "levels" / set_name / f"level{level_num}")

        with open(level_path, 'r') as f:
            for row in f.read().splitlines():
                self.matrix.append(list(row))

    def __del__(self):
        "Destructor to make sure object shuts down, etc."

    def getMatrix(self):
        return self.matrix

    def addToHistory(self, matrix):
        self.matrix_history.append(copy.deepcopy(matrix))

    def getLastMatrix(self):
        if len(self.matrix_history) > 0:
            lastMatrix = self.matrix_history.pop()
            self.matrix = lastMatrix
            return lastMatrix
        else:
            return self.matrix

    def getPlayerPosition(self):
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                if cell == "@":
                    return x, y
        return None


    def getBoxes(self):
        boxes = []
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                if cell == "$":
                    boxes.append([x, y])
        return boxes

    def getSize(self):
        return [max(len(row) for row in self.matrix), len(self.matrix)]
