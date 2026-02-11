# Part 2: 1 Programming terminology

#Exercise Fix the syntax

number = int(input("Please type in a number: "))

if number>100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!")

# Number of characters in a string

word = input("Please type in a word: ")

if len(word) > 1:
    length = len(word)
    print(f"There are {length} letters in the word {word}")
print("Thank you!")

# Typecasting

number = float(input("please type in a number: "))
integer = int(number)
decimal = number - integer

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")

# age of maturity

age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

# greater than or equal to
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the another number: "))

if num1 > num2:
    print(f"The greater number was: {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
else:
    print("The numbers are equal!")

# the elder

name1 = input("Name: ")
age1 = int(input("Age: "))
name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")

# alphabetically last
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")


# Age check

age = int(input("What is your age?"))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age <= 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")


# Nephews

name = input("please type in your name: ")

if name == 'Huey' or name == 'Dewey' or name == 'Louie':
    print("I think you might be one of Donald Duck's nephews.")
elif name == 'Morty' or name == 'Ferdie':
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")


# Grades and points

grade = int(input("How many points [0-100]: "))

if grade < 0 or grade > 100:
    print("Grade: impossible!")
elif grade >= 90 and grade <= 100:
    print("Grade: 5")
elif grade >= 80 and grade <= 89:
    print("Grade: 4")
elif grade >= 70 and grade <= 79:
    print("Grade: 3")
elif grade >= 60 and grade <= 69:
    print("Grade: 2")
elif grade >= 50 and grade <= 59:
    print("Grade: 1")
elif grade >= 0 and grade <= 49:
    print("Grade: fail")

#  fizzbuzz

num = int(input("Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("")