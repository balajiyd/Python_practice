def is_palindrome(s):
    s = s.lower()
    length = len(s)

    for i in range(length//2):
        if(s[i] != s[length - i - 1]):
            return False

    return True
w = input('Enter the word: ')
if is_palindrome(w):
    print("Y")
else:
    print("N")
