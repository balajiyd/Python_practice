def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - i - 1]:
            return False
    return True

n = int(input("Enter the number: "))
if is_palindrome(n):
    print("Y")
else:
    print("N")
