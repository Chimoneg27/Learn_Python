# print numbers

num = 2

while num <= 30:
  if num % 2 == 0:
      print(num)
  num+=1

# fix the code countdown

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
  print(number)
  number -= 1
print("Now!")

# numbers

num = int(input("Upper limit: "))
start = 1
while start < num:
    print(start)
    start += 1

# powers of two

limit = int(input("Upper limit:"))
start = 1

while start <= limit:
    print(start)
    start = start * 2

# powers of base n

limit = int(input("Upper limit:"))
base = int(input("Base:"))
start = 1

while start <= limit:
    print(start)
    start = start * base