from pathlib import Path
import json

path = Path(__file__).parent / 'characters.json'


characters = {
    "characters": [
      {'name': "Mario", 'age': 25},
      {'name': "Luigi", 'age': 24},
      {'name': "Peach", 'age': 22},
      {'name': "Bowser", 'age': 30},
      {'name': "Toad", 'age': 20},
      {'name': "Yoshi", 'age': 21},
      {'name': "Wario", 'age': 28},
      {'name': "Waluigi", 'age': 27}
    ]
  }

def write_json():
  with path.open('w') as file:
    json.dump(characters, file, indent=2)
  return

def read_json():
  with path.open('r') as file:
    data = json.load(file)
  return data

def main():
  write_json()
  data = read_json()
  print(data)

if __name__ == "__main__":
  main()
