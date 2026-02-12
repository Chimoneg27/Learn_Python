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