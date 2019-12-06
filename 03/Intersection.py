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
        x1 = self.P1.getX()
        y1 = self.P1.getY()
        x2 = self.P2.getX()
        y2 = self.P2.getY()
        x3 = self.P3.getX()
        y3 = self.P3.getY()
        x4 = self.P4.getX()
        y4 = self.P4.getY()

        dx1 = x2-x1
        dy1 = y2-y1
        dx2 = x4-x3
        dy2 = y4-y3
        
        det = (-dx1 * dy2 + dy1 * dx2)

        if det == 0:
            return Point(0,0)

        DETinv = 1.0/det

        r = DETinv * (-dy2 * (x2-x1) + dx2 * (y2-y1))
        s = DETinv * (-dy1 * (x2-x1) + dx1 * (y2-y1))
        
        ix = (x1 + r*dx1 + x2 + s*dx2)/2.0
        iy = (y1 + r*dy1 + y2 + s*dy2)/2.0

        return Point(ix, iy)

    def __repr__(self):
        return str(self.getPoint1()) + " " + str(self.getPoint2()) + " " + str(self.getPoint3()) + " " + str(self.getPoint4())