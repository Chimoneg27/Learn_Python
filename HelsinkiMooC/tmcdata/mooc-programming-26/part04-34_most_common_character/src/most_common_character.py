# Write your solution here
def most_common_character(str):
  great = 0
  top = ''
  single = []
  occur = []
  for char in str:
    single.append(char)
  # return single
  
  for lett in single:
    current = single.count(lett)
    if current > great:
      great = current
      top = lett  
  return top

if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))
