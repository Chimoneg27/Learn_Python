# Copy here code of line function from previous exercise
def line(num, hash):
    print(num * hash)

def triangle(size):
    # You should call function line here with proper parameters
    num = 1
    while num <= size:
      line(num, "#")
      num += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
