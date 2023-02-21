import sys,time, pprint as p

def dq(p):
    for v in p:
        sys.stdout.write(v)
        sys.stdout.flush()
        time.sleep(.5)

def lp(o):
    for n in o:
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(1)

#this is some work ova Dict and list. im hella rusty
# dict = {key,value}



Zulu = {'Race':'Human','Orgin':'Axum','Class':'Paladin-General','LvL':'86'}
#list = [keys]
effects = ["Pry","frz","brn","slp","Ang"]

print("\n",Zulu["Race"])

print("\n",f"{Zulu['Race']} is Zulu's race.")

Zulu["Dex"] = 256
print(Zulu) #this is one way to update it
#one way to show values
print("\n",Zulu.values())
dq("\n")

for k in Zulu.keys():
    print(k)
print("\n")

for I in Zulu.items():
    print(I)
dq("\n")

print("Zulu Int is: ",  str(Zulu.get('Int', 356)))#this also checks, but if its not there instead of an error it sets the items to that input

print(list(Zulu.keys()))

for k,v in Zulu.items():#this is the book version
    print("The Keys for Zulu are: ", k, " Values are: ", v)

lp("\n")

for k,v in Zulu.items():#my lil experiment
    print("Keys ", Zulu.keys(), "The Values: ", Zulu.values())

lp("\n")

#this checks if its in a dict

print('name' in Zulu.keys())#this method is really meant to be used in the IDE

dq("\n")

Zulu.setdefault("Str", "465")#set default only works whens theres not Items. Its good insurance bc Im not going through 500 items
Zulu.setdefault("Str","1")#should basically be null
print(Zulu["Str"])
dq("\n")
message = "Got out here since den. dey be fucked up bout lil Black. I keep me pockets fat. I luv em like."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

p.pprint(count)



print("0")
