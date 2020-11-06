# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ('Oranges', 'Grapes', 'Apples')
fruits2 = tuple(('Oranges','Grapes','Apples'))
print (fruits, type)
print (fruits[1])

del fruits2

print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples','Oranges','Pears'}
print('Apples' in fruits_set)
fruits_set.add('Grapes')
fruits_set.remove('Oranges')
fruits_set.add('Grapes')
print (fruits_set)