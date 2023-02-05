#this some input stuff
message = input("Tell me something and ill repeat it: ")
print(message)
name = input("Please enter your name") #you can put strings in input but the var will be the user input
print(f"\nHello, {name}: ")
print(name)#the var
prompt = "You can leave a personalized message"
prompt += "\n What is your nickname? \n" #only do this method with int or strings not and

nickName = input(prompt)
print(f"\nThis is your nickname {nickName}. ")
print(nickName)
#the prompt and nickname input/method is better for when you got a lot of variables and need to steady call back for stuff. It save on steady typing shit
print("All im trying to do is validate input and have it change in the dict. Not as easy as i thought")
