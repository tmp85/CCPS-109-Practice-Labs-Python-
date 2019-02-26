#Returns the longest substring of a user-entered string that does not contain repeated characters
def longest_without_repeat(text):
    no_repeat_strings_set = set()
    #Iterates through all substrings of the user-entered string and adds those without repeated characters
    #to the set no_repeat_strings_set
    for i in range(0,len(text)-1,1):
        character_check_set = set()
        character_check_set.add(text[i])
        j = i
        while (j + 1 < len(text)) and (text[j+1] not in character_check_set):
            character_check_set.add(text[j+1])
            j += 1
        no_repeat_strings_set.add(text[i:j+1])
    global longest_string
    longest_string = ""
    #Returns the longest of the "no repeated character" strings in no_repeat_strings_set
    for strings in no_repeat_strings_set:
        if len(strings) > len(longest_string):
            longest_string = strings
    return longest_string
longest_without_repeat("nowisthetimeforallgoodmentocomeinaidfortheircountry")
print(f"The longest substring that does not have repeated characters \
in the entered string is '{longest_string}' and it is {len(longest_string)} characters long.")
