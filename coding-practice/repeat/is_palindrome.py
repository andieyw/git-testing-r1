def is_palindrome(s):
    left=0
    right=len(s)-1
    while left < right:
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right-=1
            continue
        if s[right].lower() !=s[left].lower():
            return False
        left+=1
        right-=1
        
    return True
        
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome(" "))                               # True