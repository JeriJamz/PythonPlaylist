#this is a lil work out from the book. Its supposed to set Finite fields
class FieldElement:

    def __init__(self,num,prime):
	if num >= prime or num < 0:
	    error = 'Num {} not in field range 0 to {}'.format(
		num, prime -1)
	    raise ValueError(error)
	self.num = num
	self.prime = prime

    def __repr__(self):
	return 'feildElement_{}({})'.format(self.prime, self.num)

    def __ep__(self, other):
	if other is None:
	    return False
	return self.num == other.num and self.prime == self.prime

    def __add__(self, other):
	if self.prime != other.prime:
	    raise TypeError('Cannot add these two numbers. They are from diffrent fields.')
	num = (self.num + other.num) % self.prime# num = (x+b) % e
	return self.__class__(num, self.prime)#this returns the class FieldElement

