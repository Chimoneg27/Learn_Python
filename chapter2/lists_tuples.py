'''
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

# joining and slicing lists
ages_one = [27, 28, 29]
ages_two = [30, 31, 32]

joined_ages = ages_one + ages_two  # concatenates the two lists
# this is a new list, ages_one is not changed
print("joined ages:", joined_ages)

ages_one.extend(ages_two)  # extends ages_one with ages_two
print("extended ages_one:", ages_one)
'''
# ages_one is now changed, it now contains all the ages, updated the variable. mutation
#  ages_two is unchanged

# slicing lists
scores = [100, 99, 25, 44, 85, 77, 64]
print('from start to index 2:', scores[:3])
print('from index 3 to end:', scores[3:])
print('from index 1 to index 4:', scores[1:5])
print('from start to 4 with step of 2:', scores[:5:2])
print('from start to end with step of 2:, scores[::2])')
print('reversing the list:', scores[::-1])  # reverses the list