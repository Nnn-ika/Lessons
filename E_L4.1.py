def palindrome(string:str):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome('hello'))
print(palindrome('hiih'))