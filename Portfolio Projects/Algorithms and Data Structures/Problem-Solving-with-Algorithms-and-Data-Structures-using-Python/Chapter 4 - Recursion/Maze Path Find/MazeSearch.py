def searchFrom(maze, startRow, startColumn):
    maze.updadatePosition(startRow, startColumn)
    # Check for base case one:
    # We have run into an obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED:
        return False
    # Success, an outside edge not occuopied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwide, use logical short circuitting to try each
    # direction in turn
    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found