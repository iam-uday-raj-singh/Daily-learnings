def is_anagram(s,t):
    frequency = {}
    if len(s) != len(t):
        return False
    else:
        for char in s:
            if char not in frequency:
                frequency[char] = 1
            else: frequency[char]+=1
        
        for char in t:
            if char in frequency:
                frequency[char]-= 1
        
        result = all(value == 0 for value in frequency.values())
        return result
        


if __name__== "__main__":
    s= input("Enter first string: " )
    t = input("Enter second string: ")
    new = is_anagram(s,t)
    print(new)
    
   