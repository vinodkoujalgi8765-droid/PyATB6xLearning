input_string = "hello, world!"

def count_vowels(input_string):
    vowels = "aeiou"
    count =0
    display_vowels = []
    for char in input_string:
        if char in vowels:
            count = count + 1
            display_vowels.append(char)
    return count, display_vowels
print(count_vowels(input_string))
