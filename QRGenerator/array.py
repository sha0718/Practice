def isSubstring(s1,s2):
    return s2 in s1
def isRotation(s1,s2):
    if len(s1) != len(s2) or not s1:
        return False
    
    combined = s1 + s1
    return isSubstring(combined ,s2)
s1 = "waterbottle"
s2 = "erbottlewat"
result = isRotation(s1 , s2)
print(result)

            









    
 









