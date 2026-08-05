# Write your solution here
nums = int(input('Please type in a positive integer: '))
neg = -1 * nums
end = nums + 1

for i in range(neg, end, 1):
  if i == 0:
    continue
  print(i)