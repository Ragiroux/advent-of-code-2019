import math 

class Asteroid(object):

    def __init__(self, angle, x, y):
      self.angle = angle
      self.x = x
      self.y = y

    def getPiAngle(self):
      #angle = self.__convertToAngle()
      #return angle if angle > 0 else angle + 2 * math.pi
      return self.__convertToAngle()

    def __convertToAngle(self):
      if "U" in self.angle or "D" in self.angle or "L" in self.angle or "R" in self.angle:
        return float(self.angle[1:])
      else:
        return float(self.angle) 
    
    def __eq__(self, other):
      return self.__class__ == other.__class__ and self.angle == other.angle

    def __hash__(self):
      return hash(self.angle)

    def __repr__(self):
      return "({},{}) : {}".format(self.x, self.y, self.__convertToAngle())
      