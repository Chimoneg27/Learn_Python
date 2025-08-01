# reading files
from pathlib import Path

'''
def read_file():
  # open file
  file = open('characters.txt', 'r')
  
  # read file
  # content = file.read()
  # print(content)
  
  lines = file.readlines()
  for line in lines:
    print(line)
  
  # close the file
  file.close()
  
  return


# writing data to files

characters = ["mario", "luigi", "peach", "bowser", "toad"]

def write_characters_to_file(filename):
  # open file in write mode
  file = open(filename, 'w+')
  # writing to the file
  for c in characters:
    file.write(c + '\n')
    
  file.seek(0, 0)
  content = file.read()
  print(content) 
  
  # closing the file
  file.close()
  return

# appending data to files 

more_characters = ["diddy kong", "donkey kong", "diddy kong jr", "king k rool", "cranky kong"]

def write_characters_to_file(filename):
  # open file in append mode
  file = open(filename, 'a+')

  # append to the file
  for c in more_characters:
    file.write(c + '\n')

  # file.seek(0, 0)
  # content = file.read()
  # print(content) 
  
  # closing the file
  file.close()
  return
'''
# working with paths
from pathlib import Path
# pathlib moduele

file = open('characters.txt', 'r')

def create_path():
  script_dir = Path(__file__).parent
  
  path = script_dir / 'characters'
  path.mkdir(parents=True, exist_ok=True)
  path = path / 'zelda.txt'
  
  file = path.open('r')
  content = file.read()
  print(content)
  
  file.close()
  path.write_text('Epona')
  # print(script_dir.parent)
  return

def main():
  create_path()
  return

if __name__ == "__main__":
  main()