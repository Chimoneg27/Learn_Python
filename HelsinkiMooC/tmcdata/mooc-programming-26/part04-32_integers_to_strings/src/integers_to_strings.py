# Write your solution here
def formatted(arr):
  new_arr = []
  for num in arr:
    new_arr.append(f'{num:.2f}')
  return new_arr

if __name__ == "__main__":
  my_list = [1.234, 0.3333, 0.11111, 3.446]
  new_list = formatted(my_list)
  print(new_list)