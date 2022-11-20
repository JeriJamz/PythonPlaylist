#idk loops

#the x is a variable of int i

for x in range(3):
    print("attempt", x + 1)#this will print the number(add + 1 it will start the count one spot up)

for x in range(5):
    print("waiting", x + 1, (x + 1 ) * ".")#this should multiply the ellpise

for x in range(1,4):#this should be like the first code
    print("attempt")

for x in range(1,10,2):
    print('waiting')

successful = False

for x in range(3):
    print("Attempt", x+ 1,(x + 1) * ".")
    if successful:
        print('All good')
        break
else:
    print("Attempts failed")

for x in range(5):
    for y in range(3):
        print(f"{x},{y}")