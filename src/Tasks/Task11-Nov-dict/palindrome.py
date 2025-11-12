name = "M a d A m "

def palindrome_char(char):
    char = char.lower()
    if char == char[::-1]:
        return True
    else:
        return False
print(palindrome_char(name))

