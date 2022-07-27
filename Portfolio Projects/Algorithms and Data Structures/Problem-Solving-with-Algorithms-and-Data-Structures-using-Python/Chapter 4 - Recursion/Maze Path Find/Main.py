from Maze import *
from MazeSearch import *

def main():
    # Create new maze from file and show on the screen
    newMaze = Maze('mazeLayoutOne.txt')
    newMaze.drawMaze()
    newMaze.updatePosition(newMaze.startRow, newMaze.startCol)
    
    # Start recursive call
    searchFrom(newMaze, newMaze.startRow, newMaze.startCol)
    # Keeps turtle window open after it completes
    newMaze.screenExit.exitonclick()

if __name__ == "__main__":
    main()