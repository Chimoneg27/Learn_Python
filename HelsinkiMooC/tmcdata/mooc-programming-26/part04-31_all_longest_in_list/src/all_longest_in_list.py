# Write your solution here
def all_the_longest(arr):
  longest_arr = []
  longest = 0
  
  for name in arr:
    if len(name) > longest:
      longest = len(name)
  
  for i in range(len(arr)):
    if len(arr[i]) == longest:
      longest_arr.append(arr[i])
  return longest_arr


if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']