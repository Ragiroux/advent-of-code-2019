from Point import Point

class Intersection(object):

    def __init__(self, p1, p2, p3, p4):
        self.P1 = p1
        self.P2 = p2
        self.P3 = p3
        self.P4 = p4

    def getPoint1(self):
        return self.P1

    def getPoint2(self):
        return self.P2

    def getPoint3(self):
        return self.P3

    def getPoint4(self):
        return self.P4

    def getIntersectionPoint(self):
        #denominator = (self.P1.getX() - self.P2.getX()) * (self.P3.getY() - self.P4.getY()) - (self.P1.getY() - self.P2.getY()) * (self.P3.getX() - self.P4.getX())
        #print("denominator: ", denominator)
        t = ((self.P1.getX() - self.P3.getX()) * (self.P3.getY() - self.P4.getY())) - ((self.P1.getY() - self.P3.getY())*(self.P3.getX() - self.P4.getX())) / (((self.P1.getX() - self.P2.getX())*(self.P3.getY() - self.P4.getY())) - ((self.P1.getY() - self.P2.getY())*(self.P3.getX() - self.P4.getX())))
        u = ((self.P1.getX() - self.P2.getX())*(self.P1.getY() - self.P3.getY())) - ((self.P1.getY() - self.P2.getY())*(self.P1.getX() - self.P3.getX())) / (((self.P1.getX() - self.P2.getX())*(self.P3.getY() - self.P4.getY())) - ((self.P1.getY() - self.P2.getY())*(self.P3.getX() - self.P4.getX())))
        print("t: ", t)
        print("u: ", u)
        ix = self.P1.getX() + t * (self.P2.getX() - self.P1.getX())
        iy = self.P1.getY() + t * (self.P2.getY() - self.P1.getY())

        return Point(ix,iy)


    def __repr__(self):
        return str(self.getPoint1()) + " " + str(self.getPoint2()) + " " + str(self.getPoint3()) + " " + str(self.getPoint4())