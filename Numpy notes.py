import numpy as np, sys
#this should run a version check
print('this is the version check for this version of numpy')
print('This version of numy is ' +np.__version__)

#This is finna focus on array basics
a = np.array([1,2,3,4,5])
print('this is the first of the np arrays----->' + str(a))
#if you where to print it with these functions
a# is jus the array
a.shape# tells you how the matrix is build, elements and dim:(5,)
a.dtype#Type of elements in an array: int32
a.ndim#number of dims:1
a.size#total number of elements
a.itemsize# size of the bytes of each elements:4
print('I am gonna print out the central obj of an array')
print('this is the shape of array a')
print(a.shape)
print('this is the dtype of array a')
print(a.dtype)
print('this is the dims of array a')
print(a.ndim)
print('this is the size of array a')
print(a.size)
print('this is the item size of array a')
print(a.itemsize)

#you can use indexes to access certain elements in an array\
print('I am gonna access the first index in array\'a\'')
print(a[0])
# you can also change an element in an array
print('Also, would be changing the second index in an array')
print('this is a before the index change')
print(a)
a[1]=7
print('this is a after the element change')
print(a)

print('|' + 'array a has reset' + '|'+ '\n|' + '      RESET      ' + '|')
a = np.array([1,2,3,4,5])
#gonna talk about the basicas of an array
print('I should of talked about this earlier. But you can visualize arrays like this')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|                                    |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|             Loading...             |')
print('|                                    |')
print('|             Loaded!!!!             |')
print('np.array([1,2,3,4,5]) --->')
print('                            ____  ')
print('                            | 1|   ')
print('                            ____   ')
print('                            | 2|   ')
print('                            ____   ')
print('                            | 3|   ')
print('                            ____   ')

print('An array can be filled with 0\'s')
b = np.zeros(2)
print(b)#this shoulf come out 2 diffrent 0's
print('Also an array can be filled with ones as below')
ba= np.ones
print(ba)
#there is also a function to pull up empty arrays that i might prefer over ones and zeros

print('this is an empty array')
print('They come a little more useful for when you need an empty array on the fly')
bb = np.empty(2)
print(bb)

