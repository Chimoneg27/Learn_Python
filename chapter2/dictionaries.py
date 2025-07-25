# dictionaries

person = {
  'name': 'yoshi',
  'age': 30,
  'height': 5.9,
  'job': 'ninja'
}

print(person['name'])  # accessing dictionary values

# methods
print(person.keys())  # returns a list of keys
print(person.values())  # returns a list of values
# returns dictionary values, they are immutable
print('age' in person.keys())
person.update({'age': 31})  # updates the value of age
person.update({'name': 'Garvin Chimone', 'job': 'immortal'})  # updates the value of name