# Write your solution here
def sum_of_positives(arr):
  total = 0
  for i in range(len(arr)):
    if arr[i] > 0:
      total += arr[i]
  print(total)
  return total

if __name__ == "__main__":
  sum_of_positives([1, -2, 3, -4, 5])