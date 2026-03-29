def is_palindrome(s):
    clean_s=""
    for char in s:
        if char.isalnum(): #method to delete all non-letters???
            clean_s=clean_s+char.lower()  #method to make s lowercase cause ignore
        
    s=clean_s #dont need this next time
    
    left=0
    right=len(s)-1
    
    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome(" racec'ar"))
print(is_palindrome("Poop"))
print(is_palindrome("green"))


