#this the change shit to dictinary code
import ast,pprint
orginal_string = '{"John": 1, "Kan":15,"ksa":12}'

#print orginal string
print('orginal string is '+ str(orginal_string))
pprint.pprint(orginal_string)

# use ast.literal_eval() method
outcome = ast.literal_eval(orginal_string)

# print outcome
print('the dictionary is : ' + str(outcome))
