# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1,2,3,4,5]
# numbers2 = list((1,2,3,4,5))
fruits = ['Apples','Oranges','Grapes']
# print (numbers, fruits)
fruits.append("Pears")
fruits.remove("Apples")
fruits.insert(1,"Strawberry")
fruits.pop(3)
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
print(fruits)