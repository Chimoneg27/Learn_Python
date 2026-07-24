# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num, hash):
    print(num * hash)

def shape(size1, char1, size2, char2):
    num = 1
    while num <= size1:
        line(num, char1)
        num += 1
#################################################
    num2 = 0
    while num2 < size2:
        line(size1, char2)
        num2 += 1

if __name__ == "__main__":
    shape(5, "x", 3, "*")