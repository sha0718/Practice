def rotation_index(str1, str2):
    # Check if the lengths of both strings are the same
    if len(str1) != len(str2):
        return -1

    # Create a concatenated version of the first string
    double_str1 = str1 + str1

    # Find the index of str2 in the concatenated string
    index = double_str1.find(str2)

    # If the index is found, return it; otherwise, return -1
    return index if index != -1 else -1

# Example usage
print(rotation_index("coffee", "eecoff"))  # Output: 2
print(rotation_index("eecoff", "coffee"))  # Output: 4
print(rotation_index("moose", "Moose"))    # Output: -1
print(rotation_index("isn't", "'tisn"))     # Output: 2
print(rotation_index("Esham", "Esham"))     # Output: 0
print(rotation_index("dog", "god"))         # Output: -1







            


 






    
 









