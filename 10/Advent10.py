from copy import copy, deepcopy
import math 

def main():
    input = readFile("input.txt")
    grid = initializeGrid(input)
    #print(grid)
    max = deployMonitoringStation(grid)
    print("maximum asteroids found : ", max)


def initializeGrid(input):

    w = len(input[0])
    h = len(input)
    grid = [[0 for x in range(w)] for y in range(h)]

    for i in range(h):
        for j in range(w):
            grid[i][j] = input[i][j]

    return grid

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

def calculatePoint(grid):
    w = len(grid[0])
    h = len(grid)
    pts = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                pts += 1
    return pts

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

def readFile(filename):
    return open(filename, "r").read().split("\n")
    #return ".#..#\n.....\n#####\n....#\n...##".split("\n")

if __name__== "__main__":
    main()