def has_unique_characters(s):
    s = s.lower()
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True
string1 = "abcdef"
string2 ="hello"
print(has_unique_characters(string1))
print(has_unique_characters(string2))











    
 









