from copy import copy, deepcopy

def main():
    input = readFile("input.txt")
    grid = initializeGrid(input)
    max = deployMonitoringStation(grid)
    print("maximum asteroids found : ", max)


def initializeGrid(input):

    w = len(input[0])
    h = len(input)
    grid = [[0 for x in range(w)] for y in range(h)]

    for i in range(w):
        for j in range(h):
            grid[i][j] = input[i][j]

    return grid

def deployMonitoringStation(grid):
    w = len(grid[0])
    h = len(grid)
    pts = []
  
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                result = findBlindSpot(deepcopy(grid), x, y, x, y, 8, True)
                point = calculatePoint(result) - 1 #remove self
                pts.append(point)
                print("(x:{},y:{}) = {} found => {}".format(x,y,result, point))
                

    return max(pts)

def calculatePoint(grid):
    w = len(grid[0])
    h = len(grid)
    pts = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                pts += 1
    return pts

def findBlindSpot(grid,startX, startY, x, y, direction, canSee):
    w = len(grid[0])
    h = len(grid)
    asteroid = '#'

    #bottom-right (*2, *2) => direction 1
    #up-right (*2, /2) => direction 2
    #bottom-left (/2, *2) => direction 3 
    #up-left (/2, /2) => direction 4
    #up (+0, -1) => direction 5
    #down (+0, +1) => direction 6
    #left (-1, 0) => direction 7
    #right (+1, 0) => direction 8

    if not canSee:
        asteroid = 'X'
     
    if direction <= 0:
        return grid
    

    if direction == 5:
        if y-1 >= 0:
            #grid[x][y-1] = asteroid
            canSee = markAsteroid(grid, x, y-1, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x, y-1, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 6:
        if y+1 < h:
            #grid[x][y+1] = asteroid
            canSee = markAsteroid(grid, x, y+1, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x, y+1, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 7:
        if x-1 >= 0:
            #grid[x-1][y] = asteroid
            canSee = markAsteroid(grid, x-1, y, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x-1, y, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 8:
        if x+1 < w:
            #grid[x][y-1] = asteroid
            canSee = markAsteroid(grid, x+1, y, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x+1, y, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)

    if x == 0:
        x = 1
    if y == 0:
        y = 1

    if direction == 1:
        if x*2 < w and y*2 < h:
            #grid[x*2][y*2] = asteroid
            canSee = markAsteroid(grid, x*2, y*2, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x*2, y*2, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 2:
        if x*2 < w and int(y/2) > 0 :
            #grid[x*2][int(y/2)] = asteroid
            canSee = markAsteroid(grid, x*2, int(y/2), asteroid, canSee)
            return findBlindSpot(grid,startX, startY, x*2, int(y/2), direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 3:
        if  int(x/2) > 0 and y*2 < h:
            #grid[int(x/2)][y*2] = asteroid
            canSee = markAsteroid(grid, int(x/2), y*2, asteroid, canSee)
            return findBlindSpot(grid,startX, startY, int(x/2), y*2, direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
    if direction == 4:
        if int(x/2) > 0 and int(y/2) > 0:
            #grid[int(x/2)][int(y/2)] = asteroid
            canSee = markAsteroid(grid, int(x/2), int(y/2), asteroid, canSee)
            return findBlindSpot(grid,startX, startY, int(x/2), int(y/2), direction, canSee)
        else:
            return findBlindSpot(grid, startX, startY, startX, startY, direction-1, True)
   

def markAsteroid(grid, x, y, asteroid, canSee):
    if not canSee:
        grid[y][x] = asteroid
    elif grid[y][x] == '#':
        canSee = False
        grid[y][x] = asteroid
    return canSee

def readFile(filename):
    #return open(filename, "r").read().split("\n")
    return ".#..#\n.....\n#####\n....#\n...##".split("\n")

if __name__== "__main__":
    main()