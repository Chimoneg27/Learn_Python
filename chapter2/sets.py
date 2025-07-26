# sets - unordered & unique elements
ingredients = {'flour', 'sugar', 'eggs', 'milk', 'butter', 'flour'}
# print(ingredients)

# make a set using the set function around a list
ingredients_list = ['flour', 'sugar', 'eggs', 'milk', 'butter', 'flour']
ingredients_set = set(ingredients_list)
# print(ingredients_set)

#  add and reove methods
ingredients_set.add('vanilla')
ingredients_set.remove('sugar')
ingredients_set.discard('apple') # does not raise an error if 'apple' is not present

# joining sets (union)
set_one = {1, 2, 3}
set_two = {3, 4, 5}
union_sets = set_one.union(set_two)
# print(union_sets) 

# intersection (set of common elements)
int_set = set_one.intersection(set_two)
print(int_set)

# frozen (immutable) sets
ages = frozenset([19, 21, 35, 25])
# the set methods like add or remove will not work on a frozenset