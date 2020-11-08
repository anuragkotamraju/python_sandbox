# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
""" def sayHello(name='Sam'):
    print(f'Hi my name is {name}')


sayHello('Jack') """

# def sum(*nums): 
#     x=0
#     for i in nums:
#         x=i+x
#     return x

# print (sum(1,2,3))

def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')

myFun(first='Geeks', second='aren\'t', third='welcome')

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# getSum = lambda num1, num2 : num1+num2

# print(getSum(10,3))