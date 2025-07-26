# while loops
'''
score = 0

# while score <= 10:
#   print('Current score:', score)
#   score += 1
  
# user_input = ''

while user_input != 'q':
  user_input = input('Enter a command (q to quit): ')
  print('You entered:', user_input)


# Break and Continue
count  = 0

# break
# break out of the loop

while count < 10:
  if count == 5:
    # print('Breaking out of the loop at count:', count)
    break
  # print(count)
  count += 1


# continue
while count < 10:
  count += 1
  if count % 2 != 0:
    print(count)
    continue


# for loops with lists
names = ['yoshi', 'mario', 'luigi', 'peach']

# for name in names:
  # print(name)

for name in names:
  if(name == 'mario'):
    continue
  # print(name)

# for loop with strings

for letter in 'ninja':
  print(letter.upper())
  '''
# ranges in loops

# for loops with range

# for i in range(5):
#   print('Iteration:', i)

# for i in range(10, 20):
#   print(i)

for i in range(10, 20, 2): # step by 2
  print(i)
  
# negative steps

for i in range(10, 0, -1): # step by -1
  print(i)
  # the natural step is to go up 