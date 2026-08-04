# Write your solution here

arr = [1,2,3,4,5]
while True:
  num = int(input('Index: '))
  
  if num == -1:
    break
  
  new_val = int(input("New value: "))

  if num < 0 or num >= len(arr):
    print("Index is out the range of the list")
    continue

  arr[num] = new_val
  print(arr)