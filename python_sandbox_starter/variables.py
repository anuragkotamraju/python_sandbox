# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x,y,isTrue,name = (1,34.66, True, "jon")
print (x,y,isTrue,name)
print (type(x))
y = int(y)
z = float(y)
print (type(y),y)
print (type(z),z)