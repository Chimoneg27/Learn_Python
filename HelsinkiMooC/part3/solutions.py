# 1 Loops with conditionals

# Exercise: Print Numbers
start = 2

while start <= 30:
    print(start)
    start += 2

# Exercise: Fix the code Countdown

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")

# Exercise: Numbers
number = int(input("Upper limit"))
nil = 0
init = 1
while init < number:
    print(init)
    init += 1

# Exercise: Powers of two

limit = int(input("Upper limit: "))
start = 1

while start <= limit:
    print(start)
    start = start * 2

# Exercise: Powers of base n
limit = int(input("Upper limit: "))
base = int(input("Base: "))
start = 1

while start <= limit:
    print(start)
    start = start * base

# Exercise: The sum of consecutive numbers, version 1

limit = int(input("Limit: "))
total = 0
current_num = 1

while total < limit:
    total += current_num
    current_num+=1
print(total)

# Exercise: The sum of consecutive numbers, version 2
limit = int(input("Limit: "))
total = 0
current_num = 1
string = "The consecutive sum:"

while total < limit:
    total += current_num
    string += f" {current_num} +"
    current_num+=1

string = string[:-2]
print(f"{string} = {total}")