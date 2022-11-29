def checkIfNextToSolution(matriz, ycoordinate, xcoordinate):
    """
    Check if the current position is next to the solution
    :param matriz: any 2D matrix of any size
    :param xcoordinate: the x coordinate of the current position
    :param ycoordinate: the y coordinate of the current position
    :return: True if the current position is next to the solution, False otherwise
    """
    if matriz[xcoordinate][ycoordinate - 1] == 'S' or \
            matriz[xcoordinate - 1][ycoordinate] == 'S' or \
            matriz[xcoordinate][ycoordinate + 1] == 'S' or \
            matriz[xcoordinate + 1][ycoordinate] == 'S':
        return True
    else:
        return False
        
maze = [['x', 'x', 'x', 'x', 'x', 'x'],
             ['x', ' ', ' ', ' ', 'S', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', ' ', ' ', 'x'],
             ['x', ' ', 'x', ' ', 'x', 'x'],
             ['x', ' ', ' ', 'E', ' ', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x']]
             
pathUp = False 
pathRight = False
pathDown = False
pathLeft = False 

numberOfPaths = 0

row = 0 
while row < len(maze):
    col = 0
    while col < len(maze[0]):
        if (maze[row][col]) == 'E':
            entranceRow = row
            entranceCol = col 
        col += 1
    row += 1

currentLocationX = entranceRow
currentLocationY = entranceCol

entranceX= 4
entranceY = 7 

while checkIfNextToSolution (maze, currentLocationX, currentLocationY) is False: 
    
    if maze[currentLocationY-1][currentLocationX] == " ":
        pathUp = True
        numberOfPaths += 1 

    if maze [currentLocationY][currentLocationX-1] == " ":
        pathRight = True 
        numberOfPaths += 1 

    if maze [currentLocationY+1][currentLocationX] == " ":
        pathDown = True
        numberOfPaths += 1

    if maze [currentLocationY][currentLocationX+1] == " ":
        pathLeft = True 
        numberOfPaths += 1
    
    if pathUp is True: 
        maze[currentLocationY-1][currentLocationX] = "."
        currentLocation -= 1 

    if pathRight is True:
        maze [currentLocationY][currentLocationX-1] = "."
        currentLocation -= 1
        
    if pathDown is True: 
        maze[currentLocationY+1][currentLocarionX] = "."
        currentLocation -= 1

    if pathLeft is True:
        maze [currentLocationY][currentLocationX+1] = "."
        currentLocation -= 1
    
    if numberOfPaths > 1:
        chechpointX = entranceRow
        checkpointY = entranceCol

    
if checkIfNextToSolution (maze ,currentLocationX,currentLocationY) == True: 
    print ("you got out of the maze")
    print ("it took", numberOfPaths, "steps to reach the exit")