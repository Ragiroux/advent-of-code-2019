from Asteroid import Asteroid
import numpy as np
import math 


def main1():
    print("### PART 1 ###")
    input = readFile("input.txt")
    grid = initializeGrid(input)
    max = deployMonitoringStation(grid)
    print("maximum asteroids found : ", max)
    print("### END    ###")

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
                if len(result)-1 == 282:
                    print("(x:{}, y:{})".format(x,y))
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
    destoyedCounter = 0
    lastAsteroid = Asteroid(0,0,0)

    input = readFile("input.txt")
    grid = initializeGrid(input)

    asteroids = findAsteroids(grid, 22, 19)
    asteroids = sorted(asteroids, key=lambda a: a.getPiAngle(), reverse=False)
    targets = target(asteroids)
    closest = find_nearest(targets, math.pi/2)

    i = find_index(targets, closest)

    while destoyedCounter < 200: 
        lastAsteroid = targets[i]
        destoyedCounter += 1
        i -= 1
        
    print("Last asteroid to be destroyed = {} ; value = {}".format(lastAsteroid, lastAsteroid.x*100 + lastAsteroid.y))
    print("### END    ###")

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x.getPiAngle() not in unique_list: 
            unique_list.append(x.getPiAngle()) 
    return unique_list

def target(asteroids):
    uniqueAngle = unique(asteroids)
    targets = []
    
    for angle in uniqueAngle:
        groupByAngle = []
        for asteroid in asteroids:
            if asteroid.getPiAngle() == angle:
                groupByAngle.append(asteroid)
        targets.append(min(groupByAngle, key=lambda x: find_distance(x, 22, 19)))
    return targets

def find_distance(asteroid, x, y):
    return (asteroid.x - x) + (asteroid.y - y)

def find_nearest(array,value):
  return min(array, key=lambda a: abs(a.getPiAngle()-value))

def find_index(array, closest):
  for i in range(len(array)):
    if array[i] == closest:
      return i

def findAsteroids(grid,startX, startY):
    w = len(grid[0])
    h = len(grid)
    orientation = ""
    asteroids = []

    for y in range(h):
      for x in range(w):
        if grid[y][x] == '#' and (x != startX and y != startY):
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
            asteroids.append((Asteroid(orientation + str(math.atan2(startY-y, startX-x)), x, y)))
    return asteroids

if __name__== "__main__":
    main1()
    main2()