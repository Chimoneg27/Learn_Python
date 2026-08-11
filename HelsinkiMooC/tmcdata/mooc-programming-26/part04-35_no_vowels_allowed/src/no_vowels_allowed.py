# Write your solution here
def no_vowels(str):
  new_str = []
  voweled = []
  for lett in str:
    new_str.append(lett)
  
  for char in new_str:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
      continue
    
    voweled.append(char)
  return "".join(voweled)

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))