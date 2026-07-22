# Write your solution here
while True:
  user_input = input('Editor: ')
  
  if user_input.lower() == 'visual studio code':
    print('an excellent choice!')
    break
  if user_input.lower() == 'word' or user_input.lower() == 'notepad':
    print('awful')
  else:
    print('not good')