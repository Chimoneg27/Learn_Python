# Write your solution here
def length_of_longest(arr):
  num = []
  for i in range(len(arr)):
    num.append(len(arr[i]))
  
  longest = max(num)
  return longest

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]

  result = length_of_longest(my_list)
  print(result)