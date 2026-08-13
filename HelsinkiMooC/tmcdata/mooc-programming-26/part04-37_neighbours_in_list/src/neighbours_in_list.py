# Write your solution here
def longest_series_of_neighbours(lst):
  current_streak = 1
  best_streak = 1
  
  for i in range(len(lst) -1):
    if abs(lst[i] - lst[i + 1]) == 1:
      current_streak += 1
    else:
      current_streak = 1
    
    best_streak = max(best_streak, current_streak)
  
  return best_streak

if __name__ == "__main__":
  my_list = [1, 2, 5, 4, 3, 4]
  print(longest_series_of_neighbours(my_list))