from pathlib import Path

def open_file():
  path = Path(__file__).parent / 'characters.txt'
  data = ['mario', 'luigi', 'peach', 'bowser', 'toad']
  
  # context managers --> automatically close the file
  with path.open('w') as file:
    for character in data:
      file.write(character + '\n')

def main():
  open_file()

if __name__ == "__main__":
  main()
