def LongestRepeatingSubstring(strParam):
    lenght = len(strParam)      
    maxStringLenght = int(lenght/2)
    maxString = ''
    for i in reversed(range(maxStringLenght+1)):
        words = getPermutation(strParam,1)
        print(words)
        for word in words:
            if word != '':
                firstoccurence = strParam.find(word)
                if strParam.find(word,firstoccurence, len(strParam) > 0 and len(word) > len(maxString)):
                    maxString = word
                    return f" yes {words}"
    return "no null"
def getPermutation(str,size):
    ls = list()
    for i in range(len(str)):
        item = str[i:i+1]
        if item not in ls:
            ls.append(item) 
    return ls
print(LongestRepeatingSubstring("abcdabcd"))                          
print(LongestRepeatingSubstring("aaabbbcccddd"))            
    



    

