from math import sqrt
class Vector():

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.form = '{}i^ + {}j^ + {}k^'.format(self.x,self.y,self.z)
        self.magn = sqrt((abs(self.x)**2)+(abs(self.y)**2)+(abs(self.z)**2))

    def display(self):
        print(self.form)

    def __add__(self,other):
        ox = other.x
        oy = other.y
        oz = other.z
        resx = ox+self.x
        resy = oy+self.y
        resz = oz+self.z
        res = Vector(resx,resy,resz)
        return res

    def __sub__(self,other):
        ox = other.x
        oy = other.y
        oz = other.z
        resx = ox-self.x
        resy = oy-self.y
        resz = oz-self.z
        res = Vector(resx,resy,resz)
        return res
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            resx,resy,resz = self.x*other,self.y*other,self.z*other
            res = Vector(resx,resy,resz)
            return res
        elif isinstance(other, Vector):
            ox = other.x
            oy = other.y
            oz = other.z
            resx = ox*self.x
            resy = oy*self.y
            resz = oz*self.z
            res = resx+resy+resz
            return res
        else:
            raise TypeError("Unsupported operand type!")

    def unit(self):
        if self.magn == 0:
            raise ValueError("Cannot normalize the zero vector")
        x = Vector(self.x / self.magn, self.y / self.magn, self.z / self.magn)
        return x

    def help():
        print("Vector class help:")
        print(" - display(): Display the vector in the format 'xi^ + yj^ + zk^'")
        print(" - __add__(other): Add another vector to this vector")
        print(" - __sub__(other): Subtract another vector from this vector")
        print(" - __mul__(other): Multiply by a scalar or compute the dot product with another vector")
        print(" - unit(): Return the unit vector in the same direction")
        print("Vectors will also work with +,-,* ; just like you operate integers; i.e; a+b works just fine.")
        print("If you don't know, that is.")
        
        
    



