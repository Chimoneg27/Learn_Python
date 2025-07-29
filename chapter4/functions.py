# defining functions

# def greet():
  # print('hello ninjas')

# greet()

'''def say_hello(name):
  name = 'mario'
  return 'hello ' + name

result = say_hello('mario')
print(result)'''

# variable scope

# gloabal & local variables

x = 10

'''def print_x():
  global x  # points to the global variable x
  x = 5  # this is within the function scope
  print(f'x inside the print_x function: {x}')
  
def print_y():
  y = 20
  print(f'y inside the print_y function: {y}')

print_x()
print(f'global_value of x: {x}')
print_y()'''

# arguements
'''def multiply(x, y): # positional arguments
  return x * y

print(multiply(5, 10))

# NAMED ARGUMENTS

def print_score(name, score):
  print(f'{name} scored {score} points')

# default arguments

def divide(a, b):
  return a / b

# unpacking operator

def print_total(*args):
  print(*args) # this will print out the arguements stored as a tuple/ they will be unpacked
  total = 0
  for arg in args:
    total += arg
  print(f'The total is: {total}')

print_total(50, 75)
print_total(50, 75, 100)

# keyword arguements(kwargs)

def print_ninja(**kwargs):
  print(kwargs)  # this will print out the keyword arguments as a dictionary
  
  for key, value in kwargs.items():
    print(f'{key} -- {value}')

print_ninja(name='mario', age=30, location='italy')
print_ninja(name='mario', age=30, location='italy', profession='ninja')

# return values
def square(x):
  return x * x

result = square(5)
print(result)

# returning multiple values
def get_coords():
  x = 25.5
  y = 48.2
  return x, y  # this will return the values as a tuple

a, b = get_coords()
print(a, b)  # prints the tuple (25.5, 48.2)

# using return to break out of a function
age = 25

def do_something():
  if age < 20:
    return
  print(age)
  
result = do_something()
print(result)  # prints None since the function returns nothing when age is less than 20

# main function
def main():
  print('hello from the main function')
  
if __name__ == '__main__':
  main()

# name of the file
# __main__
'''