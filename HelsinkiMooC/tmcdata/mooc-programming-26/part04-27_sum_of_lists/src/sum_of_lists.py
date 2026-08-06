# Write your solution here
def list_sum(arr1, arr2):
  combined = []
  
  for i in range(len(arr1)):
    combined.append(arr1[i] + arr2[i])
  return combined

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7, 8, 9]
  print(list_sum(a, b))