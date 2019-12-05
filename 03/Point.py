class Point(object):

    def __init__(self, x, y):
        self.X = int(x)
        self.Y = int(y)

    def getX(self):
        return int(self.X)

    def getY(self):
        return int(self.Y)

    def __repr__(self):
        return "X:" + str(self.getX()) + " y:" + str(self.getY())