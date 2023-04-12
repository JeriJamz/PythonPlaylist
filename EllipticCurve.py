#this is some book work

class Point:
    def __init__(self,x,y,z,a):
        self.a = a
        self.x = x
        self.y = y
        self.z = z
        if self.y**2 != self.x**3 + z * x + a:
            raise ValueError('{},{} is not on a curve format.'.format(x,y))

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y/
            and self.z == other.z and self.a == other.a






