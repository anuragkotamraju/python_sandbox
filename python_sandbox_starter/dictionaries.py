# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 55
}

print (person, type(person))
print (person['first_name'])
print(person.get('last_name'))

person['phone']='555-555 5555'

print(person.items())

person.pop('phone')

print(person)

person2=person.copy()

print(person2)

person['phone']='555-555-5555'

print(person2)

people = [
    {'name':'Martha', 'age':30},
    {'name':'Jon', 'age':55}
]

print(people)

print(people[0]['name'])