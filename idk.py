#Random python stuff
import time, sys
def delayprint(a):
    for z in a:
        sys.stdout.write(z)
        sys.stdout.flush()
        time.sleep(0.05)

def greetings(name):
    self.name = name
    print(f"Hello, {name}!")

delayprint("Im strill working on input validation bc you can never be too good at it\n")


print('What is your name\n')
name = input()
greetings()
