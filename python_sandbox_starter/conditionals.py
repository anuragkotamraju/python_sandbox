# If/ Else conditions are used to decide to do something based on something being true or false

x=3
y=3.0
str1 = 'Jak'
str2 = 'Jak'

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

""" if x>y:
    print (f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}') """

""" if x>y:
    print (f'{x} is greater than {y}')
elif x==y:
    print (f"{x} is equal to {y}")
else:
    print(f'{y} is greater than {x}') """

# Logical operators (and, or, not) - Used to combine conditional statements
# if x>3 and x<=10:
#     print (True)

# if x>2 or x<=10:
#     print (True)

# if not(x<2):
#     print (True)

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# numbers = [1,2,3,4]

# if y not in numbers:
#     print ('in')
# else:
#     print ('Not in')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x == y:
    print (x is y)