# Copy here code of line function from previous exercise
def line(num, hash):
    print(num * hash)

def square(size, character):
    # You should call function line here with proper parameters
    num = 0
    while num < size:
        line(size, character)
        num += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3, "x")