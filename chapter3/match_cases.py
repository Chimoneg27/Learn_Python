# match case statements
'''
belt_color = input('what is your belt color: ')

match belt_color: # like switch case in other languages
  case 'white':
    print('You are a beginner.')
  case 'red':
    print('You are an intermediate student.')
  case "blue":
    print('You are an advanced student.')
  case 'purple':
    print('You are an expert student.')
  case 'black':
    print('You are a master student.')
  case _:
    print('Unknown belt color.')
# The underscore (_) acts as a default case, similar to 'default' in switch statements.
'''
# Error handling

number = int(input('Enter a number: '))

# example 1
# try:
#   number = int(input('Enter a number: '))
#   print('you entered:', number)
# except ValueError as e:
#   print('That is not a valid number.')
#   print('Error:', e)
# finally:
#   print('completed')

# example 2
a = 10
b = 0

try:
  print(a / b)
except ZeroDivisionError as e:
  print('Error: Division by zero is not allowed.')
  print('error:', e)

print('end of the file')