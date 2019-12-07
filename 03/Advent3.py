from Point import Point
from Intersection import Intersection

def main():

    cable1 = readFile("input1test.txt")
    cable2 = readFile("input2test.txt")

    path1 = []
    path2 = []
    intersection = []
    distance = []

    calculatePath(cable1, Point(0,0), 0, path1)
    calculatePath(cable2, Point(0,0), 0, path2)

    print(path1)
    print(path2)

    for i in range(0, len(path1) - 1):
        for j in range(0, len(path2) - 1):
            collission = lineLineCollision(path1[i], path1[i+1], path2[j], path2[j+1])
            if collission :
                intersection.append(Intersection(path1[i], path1[i+1], path2[j], path2[j+1]))

    for i in intersection:
        print("Intersection : ", i)
        print("Intersection point : ", i.getIntersectionPoint())
        print("Manhattan distance : ", manhattanDistance(i.getIntersectionPoint()))
        distance.append(manhattanDistance(i.getIntersectionPoint()))

    print("Lowest distance : ", min(distance))
#
# Calculate all points
#
def calculatePath(list, previous, next, dest):

    if len(list) == next:
        return dest   
            
    op = list[next][0]

    if op == 'R':
        dest.append(Point(int(list[next][1:]) + previous.getX(), 0 + previous.getY()))
    if op == 'L':
        dest.append(Point(-int(list[next][1:]) + previous.getX(), 0 + previous.getY()))
    if op == 'U':
        dest.append(Point(0 + previous.getX(), int(list[next][1:]) + previous.getY()))
    if op == 'D':
         dest.append(Point(0 + previous.getX(), -int(list[next][1:]) + previous.getY()))

    calculatePath(list,dest[-1],next+1, dest)

def lineLineCollision(p1, p2, p3, p4):

    X1 = p1.getX()
    Y1 = p1.getY()
    X2 = p2.getX()
    Y2 = p2.getY()
    X3 = p3.getX()
    Y3 = p3.getY()
    X4 = p4.getX()
    Y4 = p4.getY()
    
    s10_x = X2 - X1
    s10_y = Y2 - Y1
    s32_x = X4 - X3
    s32_y = Y4 - Y3

    denom = s10_x * s32_y - s32_x * s10_y

    if denom == 0 : return None # collinear

    denom_is_positive = denom > 0

    s02_x = X1 - X3
    s02_y = Y1 - Y3

    s_numer = s10_x * s02_y - s10_y * s02_x

    if (s_numer < 0) == denom_is_positive : return None # no collision

    t_numer = s32_x * s02_y - s32_y * s02_x

    if (t_numer < 0) == denom_is_positive : return None # no collision

    if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive : return None # no collision

    return True

def manhattanDistance(intersectionPoint):
    return (intersectionPoint.getX() - 0) + (intersectionPoint.getY() - 0)

def readFile(filename):
    return open(filename, "r").read().split(",")

if __name__== "__main__":
    main()