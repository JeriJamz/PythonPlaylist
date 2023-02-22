#this is going over os stuff
#you need to open to do anything from a file, it needs one argument, the file name
with open('numbers.txt') as file_object:#4 this method to wrk, it has to be in the same folder
    contents = file_object.read()#read() is like a f""
print(contents)#close() is how to end the read
#a bad close can corupt the file
#pie does auto close()

