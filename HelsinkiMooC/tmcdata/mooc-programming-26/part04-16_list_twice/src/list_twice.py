# Write your solution here

arr = []

while True:
  item = int(input('New item: '))
  
  if item == 0:
    print('Bye!')
    break

  arr.append(item)
  print(f'The list now: {arr}')
  sort_arr = sorted(arr)
  print(f'The list in order: {sort_arr}')