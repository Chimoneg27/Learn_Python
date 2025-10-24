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

# Exercise: The leap year

year = int(input("Please type in a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("This is a leap year")
elif year % 4 == 0 and not year % 100 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")

# Exercise: The middle letter

let1 = input("1st letter:")
let2 = input("2nd letter:")
let3 = input("3rd letter:")

if let1 < let2 and let1 > let3:
    print(f"The letter in the middle is {let1}")
elif let1 < let3 and let1 > let2:
    print(f"The letter in the middle is {let1}")
elif let2 < let3 and let2 > let1:
    print(f"The letter in the middle is {let2}")
elif let2 < let1 and let2 > let3:
    print(f"The letter in the middle is {let2}")
elif let3 > let1 and let3 < let2:
    print(f"The letter in the middle is {let3}")
elif let3 < let1 and let3 > let2:
    print(f"The letter in the middle is {let3}")

# Exercise: Gift tax
gift = int(input("Value of gift:"))

if gift < 5000:
    print("No tax!")
elif gift >= 5000 and gift < 25000:
    tax = 100 +((gift - 5000) * 0.08)
    print(f"Amount of tax: {tax}")
elif gift >= 25000 and gift < 55000:
    tax = 1700 + ((gift - 25000) * 0.10)
    print(f"Amount of tax: {tax}")
elif gift >= 55000 and gift < 200000:
    tax = 4700 +((gift -55000) * 0.12)
    print(f"Amount of tax: {tax}")
elif gift >= 200000 and gift < 1000000:
    tax = 22100 + ((gift - 200000) * 0.15)
    print(f"Amount of tax: {tax}")
elif gift >= 1000000:
    tax = 142100 + ((gift - 1000000) * 0.17)
    print(f"Amount of tax: {tax}")

# Part 4: Simple loops

# Exercise: Shall we continue?
while True:
    print('hi')
    cont = input("Shall we continue?")
    if cont == 'no':
        print("okay then")
        break

# Exercise: Input validation
from math import sqrt

while True:
    num = int(input('Please type in a number: '))
    if num == 0:
        print("Exiting...")
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(sqrt(num))

# Exercise: Fix the code countdown
number = 5
print("Countdown!")
while True:
  
  print(number)
  number = number - 1
  if number == 0:
    print("Now!")
    break

#Exercise: Repeat Password
passwrd1 = input("Password: ")
passwrd2 = input("Repeat password: ")

while passwrd1 != passwrd2:
    print("They do not match!")
    passwrd2 = input("Repeat password: ")
print("User account created!")

# Exercise: PIN and number of attempts
attempts = 0
while True:
    pin = int(input("PIN: "))
    attempts += 1

    if pin == 4321 and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    if pin != 4321:
        print("Wrong")
    else:
        print(f"Correct! It took you {attempts} attempts")
        break

# Exercise: The next leap year

year = int(input("Year: "))
year_track = year

leap_year = year_track % 4 == 0 and year_track % 100 != 0 or year_track % 100 == 0 and year_track % 400 == 0

if leap_year:
    year_track += 1
    leap_year = False

while not leap_year:
    leap_year = year_track % 4 == 0 and year_track % 100 != 0 or year_track % 100 == 0 and year_track % 400 == 0
    if not leap_year:
        year_track += 1

print(f"The next leap year after {year} is {year_track}")

# Exercise: Story
words = "" 
prev_word = ''
while True:
    word = input("Please type in a word: ")
    if word == 'end' or word == prev_word:    
        break
    words += word + " "
    prev_word = word
print(words)

# Exercise : Working with numbers
import statistics

arr = []
pos = []
neg = []
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number: "))
    if num == 0:
        # print('...the program asks for numbers')
        break
    arr.append(num)
    if num > 0:
        pos.append(num)
    if num < 0:
        neg.append(num)
print(f"Numbers typed in {len(arr)}")
print(f"The sum of the numbers is {sum(arr)}")
print(f"The mean of the numbers is {float(statistics.mean(arr))}")
print(f"Positive numbers {len(pos)}")
print(f"Negative numbers {len(neg)}")
