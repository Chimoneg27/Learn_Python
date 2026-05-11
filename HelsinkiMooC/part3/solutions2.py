# substrings part 1
word = input("Please type in a string: ")

for i in range(len(word)):
    print(word[:i+1])

# substrings part 2
word = input("Please type in a string: ")

for i in range(len(word)):
    print(word[-i-1:])

# does it contain vowels?

word = input("Please type in a string")

if 'a' in word:
    print('a found')
else:
    print('a not found')

if 'e' in word:
    print('e found')
else:
    print('e not found')

if 'o' in word:
    print('o found')
else:
    print('o not found')

# Find the first substring

word = input("Please type in a word: ")
char = input("Please type in a character: ")

pos = word.find(char)
three = word[pos:][:3]


if pos == -1:
    print('')
elif len(three) < 3:
    print('')
else:
    print(word[pos:][:3])

# find all the substrings

string = input("Please type in a word:")
char = input("Please type in a character:")
pos = string.find(char)
index = 0

while index < len(string):
    if pos == -1:
        break
    if string[index] == char:
        if len(string[index:]) >= 3:
            print(string[index:][:3])
    index = index + 1

# find the second occurrence of the substring
word = input('Please type in a string: ')
sub = input('Please type in a substring: ')

pos = word.find(sub, word.find(sub) + len(sub))

if pos != -1:
    print(f"The second occurrence of the substring is at index {pos}.")
else:
    print("The substring does not occur twice in the string.")