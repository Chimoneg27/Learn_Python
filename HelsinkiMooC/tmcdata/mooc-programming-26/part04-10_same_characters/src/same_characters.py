# Write your solution here
# You can test your function by calling it within the following block
def same_chars(str, num1, num2):
    # print(str[num1] == str[num2])
    if num2 >= len(str) or num1 >= len(str):
        return False
    
    return str[num1] == str[num2]

if __name__ == "__main__":
    print(same_chars("coder", 1, 10))