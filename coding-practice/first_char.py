#first char that only occurs once in the string

def first_char(s):
    #check all letters starting from i to 0
    #if seen reset to i+=1
    seen={}
    for char in s:
        seen[char]=seen.get(char,0)+1
        
    for i, char in enumerate(s):
        if seen[char] ==1:
            return i
         
     
print(first_char("leetcode"))     # 0
print(first_char("loveleetcode")) # 2
print(first_char("aabb"))         # -1