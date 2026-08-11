# Write your solution here
def everything_reversed(lst):
  new_list = []
  for wrd in lst:
    new_list.append(wrd[::-1])
  return new_list[::-1]

if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)