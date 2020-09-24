import pygame
import time
from cell import Cell
from nav import Solver

ln = 500
wd = 500

window = pygame.display.set_mode((ln, wd))
done = False
white = (255,255,255)
darkGrey = (100,100,100)
cellLn = int(ln/25)
cellWd = int(ln/25)

cells = [[0 for _ in range(cellLn)] for _ in range(cellWd)]

for i in range(cellLn):
    for j in range(cellWd):
        cells[i][j] = Cell(i*25, j*25, window)

wallCells = [
    cells[9][0],
    cells[9][1],
    cells[9][2],
    cells[9][4],
    cells[9][5],
    cells[9][6],
    cells[9][7],
    cells[9][8],
    cells[9][9],
    cells[9][10],
    cells[9][11],
    cells[9][12],
    cells[9][13],
    cells[9][14],
    cells[9][15],
    cells[9][16],
    cells[9][17],
    cells[9][18],
    cells[9][19]
]

solver = Solver(cells, cells[0][0], cells[19][19], wallCells)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    window.fill(white)

    #PATH CELLS ARE LIGHT GREY
    for cell in solver.pathCells:
        cell.color = (200,200,200)
    
    solver.start.color = (200,200,200)

    for i in range(cellLn):
        for j in range(cellWd):
            cells[i][j].create()

    if not solver.done:
        solver.move()

    time.sleep(.1)
        
    
    pygame.display.flip()
