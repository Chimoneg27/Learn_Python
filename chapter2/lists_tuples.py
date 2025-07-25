# lists
names = ['Garvin', 'McCready', 'luigi']  # list of strings

print(names[0])
print(names[1])
print('the length of the list is', len(names))

# changing list values
names[0] = 'Garvin Chimone'
print(names)


# list methods
names.append('Clipse')
print(names)
names.remove('luigi')
print(names)
names.sort()  # sorts the list in place
print(names)


# tuples
top_scores = (100, 95, 90, 88, 88, 85, 85)  # tuple of integers
print(top_scores)

# tuples are immutable


# tuple methods
print(top_scores.count(88))  # counts how many times 88 appears in the tuple
print(top_scores.index(90))  # finds the index of the first occurrence of 90
