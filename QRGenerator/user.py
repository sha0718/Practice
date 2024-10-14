def Stringchalllenge(strParam):
    if (strParam is not None):
        words = strParam.split(" ")
        return len(words) 
    else:
        return 0
print(Stringchalllenge("hello world")) 
print(Stringchalllenge("never eat shreddded wheat with bread"))              
print(Stringchalllenge("king of kings"))