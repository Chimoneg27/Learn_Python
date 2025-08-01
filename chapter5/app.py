from pathlib import Path

def open_file():
  path = Path(__file__).parent
  path = path / 'does' / 'not' / 'exist.txt'
  
  path.open('r')
  try:
    file = path.open('r')
    content = file.read()
    print(content)
    file.close()
  except FileNotFoundError:
    print(f"File not found: {path}")
  except Exception as e:
    print(f"An error occurred: {e}")

def main():
  open_file()

if __name__ == "__main__":
  main()