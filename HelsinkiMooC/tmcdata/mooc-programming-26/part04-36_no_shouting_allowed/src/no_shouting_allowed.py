# Write your solution here
def no_shouting(arr):
  new_list = []
  
  for str in arr:
    if str.isupper() == False:
      new_list.append(str)
  return new_list


if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)