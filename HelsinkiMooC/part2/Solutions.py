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

# Part 2: More Conditionals

# Exercise: Age of maturity

age = int(input("How old are you? "))

if age <18:
    print("You are not of age!")
else:
    print("You are of age!")

# Exercise: Greater than or equal to

first_num = int(input("Please type in the first number: "))
second_num = int(input("Please type in another number: "))

if first_num > second_num:
    print(f"The greater number was: {first_num}")
elif second_num > first_num:
    print(f"The greater number was: {second_num}")
else:
    print("The numbers are equal!")
    
# Exercise: The elder

person1 = input("Person 1: ")
age1 = int(input("Age: "))
person2 = input("Person 2: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {person1}")
elif age2 > age1:
    print(f"The elder is {person2}")
elif age1 == age2:
    print(f"{person1} and {person2} are the same age")

