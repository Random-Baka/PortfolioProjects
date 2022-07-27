from Maze import *
from MazeSearch import *

newMaze = Maze('mazeLayoutOne.txt')
newMaze.drawMaze()
newMaze.updatePosition(newMaze.startRow, newMaze.startCol)

searchFrom(newMaze, newMaze.startRow, newMaze.startCol)
newMaze.screenExit.exitonclick()