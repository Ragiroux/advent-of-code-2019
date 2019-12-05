class Point(object):

    def __init__(self, x, y):
        self.X =x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def __repr__(self):
        return "X:" + str(self.getX()) + " y:" + str(self.getY())