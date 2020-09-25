import sys

class Solver:
    grid = None
    start = None
    goal = None
    curr = None
    openCells = []
    closedCells = []
    pathCells = []
    wallCells = []
    done = False

    def __init__(self, grid, start, goal, wallCells):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.curr = start
        self.openCells.append(self.start)
        self.start.h = 0
        self.start.g = 0
        self.goal.color = (255, 255, 255)
        self.wallCells = wallCells
        for cell in wallCells:
            self.closedCells.append(cell)

    def getLeastF(self):
        lowF = sys.maxsize
        select = None
        for cell in self.openCells:
            f = cell.g + cell.h
            if f < lowF and cell not in self.closedCells:
                lowF = f
                select = cell
        return select

    def calcDist(self, cell1, cell2):
        return abs(cell1.x - cell2.x)+abs(cell1.y-cell2.y)

    def move(self):
        q = self.getLeastF()
        q.occupy()
        self.openCells.remove(q)
        self.closedCells.append(q)

        successors = []

        for i in range(q.x/25-1, q.x/25+2):
            for j in range(q.y/25-1, q.y/25+2):
                if (i != q.x/25 or j != q.y/25) and (0 <= i <= 19) and (0 <= j <= 19):
                    successors.append(self.grid[i][j])

        for cell in successors:
            if cell.parent is None and cell is not self.start:
                cell.parent = q
        
        if q == self.goal:
            self.done = True
            cCell = q
            while cCell.parent is not None:
                self.pathCells.append(cCell)
                cCell = cCell.parent
            print("Done!")

        for cell in successors:

            if cell in self.closedCells:
                continue
            
            cell.g = q.g + self.calcDist(cell, q)
            cell.h = self.calcDist(cell, self.goal)
            
            for openCell in self.openCells:
                if cell == openCell and cell.g > openCell.g:
                    continue

            self.openCells.append(cell)

        #OPEN CELLS ARE GREEN
        for cell in self.openCells:
            cell.color = (0,255,0)
        
        #CLOSED CELLS ARE BLUE
        for cell in self.closedCells:
            cell.color = (0,0,255)

        #WALL CELLS ARE BLACK
        for cell in self.wallCells:
            cell.color = (0,0,0)
        
        self.goal.color = (255, 255, 255)