from Point import Point

def main():

  cable1 =  open("input1.txt", "r").read().split(",")
  cable2 =  open("input2.txt", "r").read().split(",")

  cableCoordinate1 = []
  cableCoordinate2 = []
  dest = []

  xyz(cable1, Point(0,0), 0, dest)

  for c in cable1:
    cableCoordinate1.append(addToPointList(c)) 

  for c in cable2:
    cableCoordinate2.append(addToPointList(c))

  print(cableCoordinate2)

def xyz(list, previous, next, dest):

    op = list[next][0]

    if op == 'R':
        dest.append(Point(int(list[next][1:]) + previous.getX(), 0 + previous.getY()))
    if op == 'L':
        dest.append(Point(-int(list[next][1:]) + previous.getX(), 0 + previous.getY()))
    if op == 'U':
        dest.append(Point(0 + previous.getX(), int(list[next][1:] + previous.getY())))
    if op == 'D':
         dest.append(Point(0 + previous.getX(), -int(list[next][1:] + previous.getY())))

    xyz(list,dest[-1],next+1, dest)      


def addToPointList(cablePoint):
    op = cablePoint[0]

    if op == 'R':
        return Point(int(cablePoint[1:]),0)
    if op == 'L':
        return Point(-int(cablePoint[1:]),0)
    if op == 'U':
        return Point(0,int(cablePoint[1:]))
    if op == 'D':
         return Point(0,-int(cablePoint[1:]))

if __name__== "__main__":
  main()