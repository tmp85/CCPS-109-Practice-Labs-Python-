#Returns the longest substring of two user-entered strings

#Utility function that creates a set of the substrings of a string 
def extract_substrings(string):
    substrings = set()
    for i in range(len(string)):
        j = i
        while (j <= len(string)):
            substrings.add(string[i:j])
            j += 1
    return substrings

#Returns the longest string common to two sets
def longest_common_substring(text1, text2):
    text1_substrings = extract_substrings(text1)
    text2_substrings = extract_substrings(text2)
    common_substrings = text1_substrings.intersection(text2_substrings)
    longest_string = ""
    for strings in common_substrings:
        if len(strings) > len(longest_string):
            longest_string = strings
    return longest_string

#Test with "abcd" and "abdefg", which returns "ab"
print(longest_common_substring("abcd","abdefg"))
