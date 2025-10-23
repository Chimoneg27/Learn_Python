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


# Part 2: combining conditionals

# Exercise: Age 
age = int(input("What is your age?"))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age < 5 and age > -1:
    print(f"I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# Exercise: Nephew's
name = input("Please type in your name: ")

if name == 'Huey' or name == 'Dewey' or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == 'Morty' or name == 'Ferdie':
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Exercise: Grade and points

score = int(input("How many points [0-100]:"))

if score < 0 or score > 100:
    print("Grade: impossible!")
elif score >= 0 and score < 50:
    print(f"Grade: fail")
elif score >= 50 and score < 60:
    print(f"Grade: 1")
elif score >= 60 and score < 70:
    print(f"Grade: 2")
elif score >= 70 and score < 80:
    print(f"Grade: 3")
elif score >= 80 and score < 90:
    print(f"Grade: 4")
elif score >= 90 and score <=100:
    print(f"Grade: 5")

# Exercise: FizzBuzz
number = int(input("Number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("")