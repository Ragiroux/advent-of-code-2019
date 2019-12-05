from Point import Point

def main():

  cable1 = readFile("input1.txt")
  cable2 = readFile("input2.txt")

  path1 = []
  path2 = []

  calculatePath(cable1, Point(0,0), 0, path1)
  calculatePath(cable2, Point(0,0), 0, path2)

  print("path1 : ", path1)
  print("path2 : ", path2)

#
# Calculate all points and add the previous point
#
def calculatePath(list, previous, next, dest):

    if len(list) == len(dest):
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

def readFile(filename):
    return open(filename, "r").read().split(",")

if __name__== "__main__":
  main()