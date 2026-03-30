def sorted_valid_anagram(s,t):
    if sorted(s) == sorted(t):
        return True
    return False



def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    word = {}
    
    #what letters exist in s and how many of each
    for char in s:
        word[char]=word.get(char,0)+1
        
    #compare with whats in t with s
    for char in t:
        if char not in word or word[char] == 0:
            return False
        word[char]-=1 #check if letter count matchs work backwards
            
    return True
    
    
print(valid_anagram("car", "rac")) #True
print(valid_anagram("great", "regat")) #True
print(valid_anagram("grin", "irne")) #False
#more letters
print(valid_anagram("grin", "irngg")) #False 
#no letters
print(valid_anagram("", "")) #True

#caps
#non-char

