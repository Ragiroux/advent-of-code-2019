from Point import Point
from Intersection import Intersection

def main():

    cable1 = readFile("input1test.txt")
    cable2 = readFile("input2test.txt")

    path1 = []
    path2 = []
    intersection = []

    calculatePath(cable1, Point(0,0), 0, path1)
    calculatePath(cable2, Point(0,0), 0, path2)

    print("cable 1 : ", path1)
    print("cable 2 : ", path2)

    for i in range(0, len(path1)-1):
        for j in range(0, len(path2)-1):
            collission = lineLineCollision(path1[i], path1[i+1], path2[j], path2[j+1])
            if collission :
                intersection.append(Intersection(path1[i], path1[i+1], path2[j], path2[j+1]))

    for i in intersection:
        print("Intersection : ", i)
        print("Manhattan distance : ", manhattanDistance(i.getIntersectionPoint()))


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

    denominator = ((p2.getX() - p1.getX()) * (p4.getY() - p3.getY())) - ((p2.getY() - p1.getY()) * (p4.getX() - p3.getX()))
    numerator1 = ((p1.getY() - p3.getY()) * (p4.getX() - p3.getX())) - ((p1.getX() - p3.getX()) * (p4.getY() - p3.getY()))
    numerator2 = ((p1.getY() - p3.getY()) * (p2.getX() - p1.getX())) - ((p1.getX() - p3.getX()) * (p2.getY() - p1.getY()))

    if denominator == 0:
        return False
    
    r = numerator1 / denominator
    s = numerator2 / denominator

    return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)

def manhattanDistance(intersectionPoint):
    return (intersectionPoint.getX() - 0) + (intersectionPoint.getY() - 0)

def readFile(filename):
    return open(filename, "r").read().split(",")

if __name__== "__main__":
    main()
    