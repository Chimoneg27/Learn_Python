# Write your solution here
def even_numbers(arr):
  even = []
  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      even.append(arr[i])
  return even

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print('original', my_list)
  print('new', even_numbers(new_list))