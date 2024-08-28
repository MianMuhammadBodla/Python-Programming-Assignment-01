# String Splitting and Joining

# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
# s:str ="apple,banana,cherry,dates"
# Expected Output:
# ["apple", "banana", "cherry", "dates"]
# apple banana cherry dates


# Solution:


s:str ="apple,banana,cherry,dates"

substrings = s.split(',')

formatted_output = "[" + ", ".join(f'"{item}"' for item in substrings) + "]"

print(formatted_output)



joined_string = ' '.join(substrings)

print(joined_string)
