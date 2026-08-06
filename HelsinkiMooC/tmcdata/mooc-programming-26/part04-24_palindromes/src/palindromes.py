# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(str):
  rev = str[::-1]
  # print(True if str == rev else False)
  return True if str == rev else False
  
while True:
  palin = input('Please type in a palindrome: ')
  rev = palin[::-1]
  
  if rev == palin:
    print(f'{palin} is a palindrome!')
    break
  print("that wasn't a palindrome")

palindromes('purps')
palindromes('dud')
