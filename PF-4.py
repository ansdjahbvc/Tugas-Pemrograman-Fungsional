a = "rotator"
def palindrome(b):
    if b == b[::-1]:
        return "true"
    else:
        return "false"
print(palindrome(a))