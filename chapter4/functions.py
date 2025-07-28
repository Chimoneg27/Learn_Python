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
