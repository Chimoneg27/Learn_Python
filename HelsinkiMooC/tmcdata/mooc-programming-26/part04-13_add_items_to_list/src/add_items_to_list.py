# Write your solution here

arr = []
size = int(input('How many items: '))
while size > 0:
  item_num = 1
  new_item = int(input(f'Item {item_num}: '))
  arr.append(new_item)

  size -= 1
  # item_num += 1
print(arr)