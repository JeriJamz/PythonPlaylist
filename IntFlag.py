#this is some time go Rflag idk but it looks likes its mainly for int but I pretty sure you can make this a bool and itll be a good flag
from enum import IntFlag, Flag, auto

class Perm(IntFlag):
    R = 4
    W = 2
    X = 10

#Perm.R | Perm.W Perm.R + Perm.W run these in the shell
RW = Perm.R | Perm.W#try  Perm.R in RW and see the bool

#flags

class Color(Flag):
    BLACK = 0 #this is 0, it also is false. The first default attr is 1(True), then it counts in power of 2
    RED = auto()#1
    BLUE = auto()#2
    GREEN = auto()#4
    WHITE = RED |  BLUE | GREEN #this is 7 tho... bc when you combine it makes it odd, handy for organization

