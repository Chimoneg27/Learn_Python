# declaring variables
name = 'McCready' # string
age = 30 # integer
height = 5.9 # float

# printing variables
# print(name, age, height)

# # type errors
# print(name + "is" + str(height) + "feet tall")
# print(name + age) # This will raise a TypeError
# python is a strongly typed language, does not allow implicit type conversion

# string methods
greeting = 'hello, ninjas'
# print(len(greeting))  # length of the string
# print(greeting.strip())
# print(greeting.replace('ninjas', 'garvin'))
# all the methods do not change the original string, they return a new one
# non destructive methods

'''
making comments
print()
'''

# fromatted strings (f-strings)
name = 'mario'
score = 50

# examples - newer
# print(f'{name} scored {score} points')

# older approach
# print("{} has a score of {}".format(name, score))
# print("{0} has a score of {1}".format(name, score))
# print("{n} has a score of {s}".format(n=name, s=score))

# expressions in f-strings
# print(f"{name.capitalize()} scored {score + 10} points")

# user input
name = input("Your name please: ") 
age =  int(input("Your age please: "))

# print(f"Hello {name}, you are {age} years old.")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"The sum of {a} and {b} is {a + b}.")