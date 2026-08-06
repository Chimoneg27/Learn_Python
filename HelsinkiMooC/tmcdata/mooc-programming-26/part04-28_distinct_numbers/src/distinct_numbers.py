# Write your solution here
def distinct_numbers(arr):
  new_set = set(arr)
  distinct = list(new_set)
  return sorted(distinct)

if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1]
  print(distinct_numbers(my_list)) # [1, 2, 3]
  print(distinct_numbers(([1, 10, 1, 100, 1, 1000])))