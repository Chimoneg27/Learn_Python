# Write your solution here
# You can test your function by calling it within the following block
def line(num, letter):
    if len(letter) == 0:
        letter = '*'
    print(num * letter[0])

if __name__ == "__main__":
    line(5, "x")