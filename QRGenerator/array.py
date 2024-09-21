def reverse_c_string(c_string):
    # Convert the input string to a list for easier manipulation
    string_list = list(c_string)
    
    # Find the index of the null character
    null_index = string_list.index('\0') if '\0' in string_list else len(string_list)
    
    # Slice the string up to the null character
    sub_string = string_list[:null_index]
    
    # Reverse the substring and append the null character
    reversed_string = sub_string[::-1] + ['\0']
    
    # Join the list back into a string
    return ''.join(reversed_string)

# Example usage
c_string = "abcd\0"
reversed_string = reverse_c_string(c_string)
print(reversed_string)  # Output should be "dcba\0"







    
 









