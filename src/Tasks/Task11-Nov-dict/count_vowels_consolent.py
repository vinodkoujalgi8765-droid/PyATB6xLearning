input_string = "hello, world!"

def count_vowels(input_string):
    vowels = "aeiou"
    count_vowels =0
    count_consonants = 0
    display_vowels = []
    display_consonants = []
    for char in input_string:
        if char in vowels:
            count_vowels = count_vowels + 1
            display_vowels.append(char)
        elif char not in vowels:
            if (char != " " or char != "!" or char != "," or char != ".") in input_string:
                count_consonants = count_consonants + 1
                display_consonants.append(char)

    print(count_vowels,display_vowels)
    print(count_consonants,display_consonants)

count_vowels(input_string)
