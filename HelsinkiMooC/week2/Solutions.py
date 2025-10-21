# Part 2: 1 Programming terminology

#Exercise Fix the syntax

number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")
else:
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")
    

#Exercise: Number of characters
word = input("Please type in a word: ")
length = len(word)

if length > 1:
    print(f"There are {length} letters in the word {word}")
print("Thank you!")

# Typecasting

number = float(input("Please type in a number: "))
integer = int(number)
decimal = number - integer

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")