from copy import copy, deepcopy
import math 

def main1():
    print("### PART 1 ###")
    input = readFile("input.txt")
    grid = initializeGrid(input)
    max = deployMonitoringStation(grid)
    print("maximum asteroids found : ", max)
    print("### END ###")

def deployMonitoringStation(grid):
    w = len(grid[0])
    h = len(grid)
    asteroids = []
  
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                result = findBlindSpot(grid, x, y)
                #print("asteroids = {}, angles = {}".format(len(result)-1, result))
                asteroids.append(len(result)-1)
    return max(asteroids)

def findBlindSpot(grid,startX, startY):
    w = len(grid[0])
    h = len(grid)
    orientation = ""
    asteroids = set([])
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                if startX == x:
                    if startY < y:
                        orientation = "D"
                    else:
                         orientation = "U"
                elif startY == y:
                    if startX < x:
                        orientation = "R"   
                    else:
                        orientation = "L"
                else:
                    orientation = ""
                asteroids.add(orientation + str(math.atan2(startY-y, startX-x)))
    return asteroids

def initializeGrid(input):
    w = len(input[0])
    h = len(input)
    grid = [[0 for x in range(w)] for y in range(h)]

    for i in range(h):
        for j in range(w):
            grid[i][j] = input[i][j]
    return grid
    
def readFile(filename):
    return open(filename, "r").read().split("\n")
    #return ".#..#\n.....\n#####\n....#\n...##".split("\n")

###############################################################################
#
#           PART 2
#
###############################################################################

def main2():
    print("### PART 2 ###")
    #282: (x:22,y:19)
    input = readFile("input.txt")
    grid = initializeGrid(input)

    w = len(grid[0])
    h = len(grid)

    result, coordinateX, coordinateY = laser(grid,22,19)
    
    print(len(result)-1)
    print(result)

    print("### END ###")

def laser(grid,startX, startY):
    w = len(grid[0])
    h = len(grid)
    orientation = ""
    asteroids = set([])
    asteroidsCoordinateX = set([])
    asteroidsCoordinateY = set([])

    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                if startX == x:
                    if startY < y:
                        orientation = "D"
                    else:
                        orientation = "U"
                elif startY == y:
                    if startX < x:
                        orientation = "R"   
                    else:
                        orientation = "L"
                else:
                    orientation = ""
                asteroids.add(orientation + str(math.atan2(startY-y, startX-x)))
    return asteroids, asteroidsCoordinateX, asteroidsCoordinateY

if __name__== "__main__":
    main1()
    main2()