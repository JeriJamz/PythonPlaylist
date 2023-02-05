#that cls is dumb important. is like you calling or changing a class(maybe its instances and atrr too). Now im starting to understand the diffrent between instances and classes
#plus you got use it like self
import time, sys
from enum import Enum
def delayprint(a):
    for z in a:
        sys.stdout.write(z)
        sys.stdout.flush()
        time.sleep(.005)


delayprint("This is something I saw in docs\n")

class Coordinate(bytes, Enum):#this limits class like in Java
    """
    Coords w/ Bin Code that can be indexed bt the int code
    """
    def __new__(cls, value, label, unit):#Have to use this w/ Enum
        obj = bytes.__new__(cls, [value])#calls bytes
        obj._value_ = value
        obj.label = label
        obj.unit = unit
        return obj#this return the 
    PX = (0, 'P.X','km')#these are the Bin Code
    PY = (1, 'P.Y','km')
    VX = (2, 'V.X','km/s')
    VY = (3, 'V.Y','km/s')

print(Coordinate['PY'])
print(Coordinate(3))
