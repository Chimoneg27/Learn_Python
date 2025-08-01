# reading files
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
  
  return'''


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

def main():
  write_characters_to_file('characters.txt')
  return

if __name__ == "__main__":
  main()