# main function
from helpers import add, multiply

def main():
  print('hello from the main function, in the app file')
  result = add(5, 10)
  print(result)
  multiply(5, 10)
  
if __name__ == '__main__':
  main()