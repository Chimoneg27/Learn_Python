# declaring variables
name = 'McCready' # string
age = 30 # integer
height = 5.9 # float

# printing variables
print(name, age, height)

# type errors
print(name + "is" + str(height) + "feet tall")
# print(name + age) # This will raise a TypeError
# python is a strongly typed language, does not allow implicit type conversion

# string methods
greeting = 'hello, ninjas'
print(len(greeting))  # length of the string
print(greeting.strip())
print(greeting.replace('ninjas', 'garvin'))
# all the methods do not change the original string, they return a new one
# non destructive methods

'''
making comments
print()
'''
