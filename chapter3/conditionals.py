score = 99
'''
# if statements
if score > 5:
  print('the score is greater than 5')

# if/else statements
if score > 10:
  print('the score is greater than 10')
else:
  print('the score is not greater than 10')


# if/elif/else statements
if score > 10:
  print('the score is greater than 10')
elif score > 5:
  print('the score is greater than 5 but not greater than 10')
else:
  print('the score is 5 or less')


#  AND, OR, NOT, IS NOT

age = 18

if age > 12 and age < 20:
  print('teenager')
  
if age < 13 or age > 19:
  print('not a teenager')
  
authenticated = False

if not authenticated:
  print('user is authenticated')
  
if authenticated is not True:
  print('user is not authenticated')
'''
score = int(input('Enter a score between 0 and 100: '))
# conditional assignment / ternary operator

is_top_score = True if score >= 90 else False
print('is_top_score:', is_top_score)

# nested ternary operator

temo = int(imput('Enter a temperature in celsius between 0 and 40:'))

weather = 'hot' if temp > 25 else ('mild' if temp > 15 else 'cold')
print('The weather is:', weather)