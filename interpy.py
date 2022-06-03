# this is for intermediate python hopefully its just a review on somethings
import time,sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def delay_print2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)


delay_print('Hello World\n')#this works but i think that it links with everytime its called

delay_print('This is lesson 1\nIt is about list\n')

delay_print2('This is lesson 1.1\n')

mylist = ['$L','IDK','Cat','Dog','a',True,12]#this is a lisr
mylist2 = list()#this will create an empty list
mylist3 = ['apple','apple','hey','dogs']# you can make duplicates but when its called python will only pull the first one that is called i think
item = mylist[0]

def list1_1():
    print(mylist)
    print(mylist2)
    print(mylist[0])#you can jus call the index like this
    delay_print('you can also call indexes with assigned variables ' + item)
    delay_print('\n also you can use the negative interger to reverse call items ')
    print(mylist[-1])
    delay_print('one way to check for items in a list is with a if loop\n')
    if 'Banana' in mylist:
        print('it is in mylist')
    else:
        print('It is not in mylist')
    if 'IDK' in mylist:
        print('it is in mylist')
    else:
        print('It is not in mylist')
    print('len method is one way to check a list \n' + str(len(mylist)))#length
    print('mylist[1:5]' + str(mylist[1:5]))
    delay_print('\nyou can add things to your list without the append method\n')
    mylist[2] = 5 
    print(str(mylist[2]))
    print('Here\'s the append method')
    mylist.append('Yen')
    print(str(mylist))
    print('Items can be deleted from list using the del method')
    print(str(mylist))
    del mylist[2]
    print(str(mylist))
    #there is also sum basics operations with list and im pretty sure itll work with dictionaries too
    delay_print('List and be concatenated together')
    mylist4 = mylist + mylist2
    mylist5 = [1,3,2,7]+[6,8,4,5]#concatenation
    print(str(mylist4))
    print(str(mylist5))
    delay_print('Also list can have repition')
    print(['Hi']*4)#repition
    #print('Max value element : ' + max(mylist))
    item2 = mylist5.sort()
    print(item2)
list1_1()
        
    
    
