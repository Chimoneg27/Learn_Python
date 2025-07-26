# booleans

is_authenticated = True

print(is_authenticated)
print(not is_authenticated)

# comparison operators
x, y = 5, 10
# print(x == y) 
# print(x != y)
# print(x < y)
# print(x > y)  
# print(x <= y)
# print(x >= y)

# boolean operators & member checking 

x, y = True, False
# print(x and y)
# print(x or y)

# falsey values --> 0 numbers and empty data structures

# print(bool(0))  # False

# truthy values --> non-zero numbers and non-empty data structures
print(bool(1))  # True
# print(bool([1, 2, 3]))  # True

# evaluate strings
name = 'Garvin Chimone'
print(name.startswith('G'))