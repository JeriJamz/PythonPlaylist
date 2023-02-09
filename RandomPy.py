#idk random stuff
import sys,time
from datta import *
def dq(q):
    for t in q:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(.05)

name = input('What is your name?')
dq(f"Hello my name is Walter, {name}\n")#My name is Walter, Jeri
dq(f"Where are my manners. Your name is {name}, is it not?\n")
response = input()

while response.lower() != 'yes':
    dq('I apologize for that. Please Renter your name again.\n')
    name = input()
    dq(f'I hope thjis clear things up. {name2}, is it.\n')
    response = input()

age = input('Please Verify your age\n')
age = int(age)

if age < 21:
    dq('You are too young to ride this ride\n')
    sys.exit()
else:
    dq('Let us continue with the shanangans\n')

dq('Let see if we can make a little datebase.\n')


    
