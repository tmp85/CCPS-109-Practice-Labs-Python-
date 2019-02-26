"""
# repeats elements in seq, dup times in a new list
seq = [1,'hello', 3]
def stutter(seq, dup):
    b = list()
    for i in range(len(seq)):
        for x in range(0,dup):
            b.append(seq[i])
    return b
print(stutter(seq,4))
"""

"""
#Returns the longest substring of a user-entered string\
#that does not contain repeated characters
def longest_without_repeat(text):
    no_repeat_strings_set = set()
    for i in range(len(text)-1):
        character_check_set = set()
        character_check_set.add(text[i])
        j = i
        while (j + 1 < len(text)) and (text[j+1] not in character_check_set):
            character_check_set.add(text[j+1])
            j += 1
        no_repeat_strings_set.add(text[i:j+1])
    global longest_string
    longest_string = ""
    for strings in no_repeat_strings_set:
        if len(strings) > len(longest_string):
            longest_string = strings
    return longest_string
longest_without_repeat("nowisthetimeforallgoodmentocomeinaidfortheircountry")
print(f"The longest substring that does not have repeated characters \
in the entered string is '{longest_string}' and it is {len(longest_string)} characters long.")
"""

"""
#Given a user-entered number 'm' and a maximum integer 'giveup', returns the smallest
#integer that ends in 'm' less than 'giveup', if one exists
def babbage(m,giveup):
    global i
    i = 0
    while i < giveup:
        if (i ** 2) % (10 ** len(str(m))) != m:
            i += 1
        else:
            print(f"The smallest integer whose square ends with {m} is {i}. {i}'s square is {i ** 2}.")
            return i
    print(f'There is no integer less than {giveup} whose square ends in {m}.')
    return -1
m = int(input("Please enter an integer to form the final digits of a squared number: "))
giveup = int(input(f"Please enter a maximun integer below which \
to check for existing squares that ends in {m}: "))
print(babbage(m,giveup))
"""

def extract_substrings(string):
    substrings = set()
    for i in range(len(string)):
        j = i
        while (j <= len(string)):
            substrings.add(string[i:j])
            j += 1
    return substrings

def longest_common_substring(text1, text2):
    text1_substrings = extract_substrings(text1)
    text2_substrings = extract_substrings(text2)
    common_substrings = text1_substrings.intersection(text2_substrings)
    longest_string = ""
    for strings in common_substrings:
        if len(strings) > len(longest_string):
            longest_string = strings
    return longest_string

#Test with "abcd" and "abdefg"
#print(longest_common_substring("abcd","abdefg"))
