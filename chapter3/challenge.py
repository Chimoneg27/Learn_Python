# CHALLENGE: Shopping list formatter

shopping_list = []

# SECTION ONE - creating the shopping list
while True:
    
  item = input("Enter an item (or 'q' to quit): ")
  if item == 'q':
    break
  
  # Challenge: ask user for price (int)
  # handle any ValueError by printing a message, skipping a loop and asking for a new item
  try:
    price = int(input("Enter the price (£) of the item: "))
  except ValueError as e:
    print('Please enter a valid number')
    continue

  shopping_list.append((item, price))

# SECTION TWO - formatting the shopping list
total = 0

for item in shopping_list:
  print(f'{item[0]} - £{item[1]}')
  total += item[1]

print(shopping_list)
print(f'your total is: £{total}')
print()

# Challenge: use a for loop to print each item and price on its own line
# after all items have been output, also print out the total price
