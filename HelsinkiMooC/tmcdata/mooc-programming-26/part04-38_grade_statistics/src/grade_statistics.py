# Write your solution here
import math
def results_from_learner():
  scores = []
  while True:
    user_input = input("Exam points and exercises completed: ")

    if not user_input.strip():
      print("Statistics:")
      break

    points, exercises = map(int, user_input.split())
    scores.append({"points": points, "exercises": exercises})
  return scores

def grade_of_learner(arr_of_obj):
  grades = []
  points_avg = []
  
  for i in range(len(arr_of_obj)):
    
    final_score = arr_of_obj[i]['points'] + math.floor(arr_of_obj[i]['exercises'] / 10)
    points_avg.append(final_score)

    if arr_of_obj[i]['points'] < 10:
      grades.append(0)
      continue
      
    if final_score >= 0 and final_score <= 14:
      grades.append(0)
    elif final_score >= 15 and final_score <= 17:
      grades.append(1)
    elif final_score >= 18 and final_score <= 20:
      grades.append(2)
    elif final_score >= 21 and final_score <= 23:
      grades.append(3)
    elif final_score >= 24 and final_score <= 27:
      grades.append(4)
    else:
      grades.append(5)

  more_than_0 = 0
  zeroes = 0
  for i in range(len(grades)):
    if grades[i] == 0:
      zeroes += 1
      continue
    more_than_0 += 1
  total = more_than_0 + zeroes
  pass_percentage = (more_than_0 / total) * 100

  avg = sum(points_avg) / len(points_avg)
  print(f"Points average: {avg:.1f}")
  print(f"Pass percentage: {pass_percentage:.1f}")
  
  distributions = { 5: '', 4: '', 3: '', 2: '', 1: '', 0: ''}
  print('Grade distribution:')
  
  for grade in grades:
    if grade in distributions:
      distributions[grade] += '*'
  
  for key, value in distributions.items():
    print(f"{key}: {value}")
  return grades

# results_from_learner()
grade_of_learner(results_from_learner())