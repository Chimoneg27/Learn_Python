# Leap year

year = int(input("Please type in a year: "))


if year % 400 == 0:
    print("That year is a leap year")
elif year % 100 == 0:
    print("That year is not a leap year")
elif year % 4 == 0:
    print("That year is a leap year")
else:
    print("That year is not a leap year.")


# alphabeticaly in the middle

let1 = input("1st letter: ")
let2 = input("2nd letter: ")
let3 = input("3rd letter: ")

letters = [let1, let2, let3]
letters.sort()

print(f"The letter in the middle is {letters[1]}")


#  gift tax

gift_amount = int(input("Value of gift: "))

if gift_amount >= 5000 and gift_amount < 25000:
    tax = 100 + ((gift_amount - 5000) *0.08)
    print(f"Amount of tax: {tax} euros")
elif gift_amount >= 25000 and gift_amount < 55000:
    tax = 1700 + ((gift_amount - 25000) *0.10)
    print(f"Amount of tax: {tax} euros")
elif gift_amount >= 55000 and gift_amount < 200000:
    tax = 4700 + ((gift_amount - 55000) *0.12)
    print(f"Amount of tax: {tax} euros")
elif gift_amount >= 200000 and gift_amount < 1000000:
    tax = 22100 + ((gift_amount - 200000) *0.15)
    print(f"Amount of tax: {tax} euros")
elif gift_amount >= 1000000:
    tax = 142100 + ((gift_amount - 1000000) *0.17)
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")


# shall we continue?

while True:
    print('hi')
    text = input("Shall we continue? ")

    if text == 'no':
        break
print("okay then")


# input validation
from math import sqrt
# Write your solution here

while True:
    num = int(input("Please type in a number: "))

    if num > 0:
        print(sqrt(num))
    elif num == 0:
        print('Exiting...')
        break
    else:
        print("Invalid number")

# fix the countdown
number = 5
print("Countdown!")
while number > 0:
  print(number)
  number = number - 1
  if number == 0:
    break

print("Now!")

# repeat password

password = input("Password:")

while True:
  repeat_password = input("Repeat password:")
  if password != repeat_password:
    print("They do not match!")
    
  if password == repeat_password:
    print("User account created!")
    break

# pin number and attempts

attempts = 0

while True:
    pin = input("PIN:")

    attempts += 1
    if pin == "4321" and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break
    if pin == "4321":
        print("Correct! It only took you one single attempt!")
        break
    print("Wrong")

# story time
words = ''
prev_word = ''
while True:
    word = input("Please type in a word:")

    if word == 'end' or word == prev_word:
        # word2 = word
        break
    words += word + " "
    prev_word = word
print(words)

# working with numbers again

print("Please type in integer numbers. Type in 0 to finish.")

num_entered = 0
total = 0
pos = 0
neg = 0
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    if num > 0:
        pos += 1
    if num < 0:
        neg += 1
    num_entered += 1
    total += num
print(f"Numbers typed in {num_entered}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / num_entered}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")