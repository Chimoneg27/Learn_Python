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
print_total(50, 75, 100)'''

# keyword arguements(kwargs)

def print_ninja(**kwargs):
  print(kwargs)  # this will print out the keyword arguments as a dictionary
  
  for key, value in kwargs.items():
    print(f'{key} -- {value}')

print_ninja(name='mario', age=30, location='italy')
print_ninja(name='mario', age=30, location='italy', profession='ninja')