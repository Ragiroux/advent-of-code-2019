from copy import copy, deepcopy

def main():
    input = readFile("input.txt")
    grid = initializeGrid(input)
    max = deployMonitoringStation(grid)
    #print("maximum asteroids found : ", max)


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
    pts = []
  
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                result = findBlindSpot(deepcopy(grid), x, y)
                print(len(result))
                #point = calculatePoint(result) - 1 #remove self
                #pts.append(point)
                #print("(x:{},y:{}) = {} found => {}".format(x,y,result, point))
                

    #return max(pts)

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
    asteroids = {}
    for y in range(h):
        for x in range(w):
            if grid[x][y] == '#':
                if x == startX:
                    slope = (startY - y)
                elif y == startY:
                    slope = (startX - x)
                else:
                    slope = (int((startY - y) / (startX - x)))
                asteroids[slope] = (startY - y) + (startX - x)
    return asteroids

def readFile(filename):
    #return open(filename, "r").read().split("\n")
    return ".#..#\n.....\n#####\n....#\n...##".split("\n")

if __name__== "__main__":
    main()