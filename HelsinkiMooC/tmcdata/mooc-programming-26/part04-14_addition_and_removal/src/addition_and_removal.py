# Write your solution here

arr = []
print(f'The list is now {arr}')
start = 0
while True:

  add_rem_exit = input('a(d)d, (r)emove or e(x)it:' )
  if add_rem_exit == 'x':
    print('Bye!')
    break
  elif add_rem_exit == 'd':
    start += 1
    arr.append(start)
    print(f'The list is now {arr}')
  elif add_rem_exit == 'r':
    start -= 1
    arr.pop()
    print(f'The list is now {arr}')
  else:
    break
  