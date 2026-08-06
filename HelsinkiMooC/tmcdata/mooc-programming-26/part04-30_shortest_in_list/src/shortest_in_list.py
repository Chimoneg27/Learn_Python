# Write your solution here
def shortest(arr):
  num = []
  for i in range(len(arr)):
    num.append(len(arr[i]))
  
  short = min(num)
  for item in arr:
    if len(item) == short:
      return item
  # model solution
  '''
  result = ''
  
  for nimi in names:
    if result == "" or len(nimi) < len(result):
      result = nimi
  return result
  '''

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = shortest(my_list)
  print(result)