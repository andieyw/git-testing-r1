def incorrect_is_valid(s):
    open=[]
    open.append("(")
    open.append("{")
    open.append("[")

    close=[]
    close.append(")")
    close.append("}")
    close.append("]")
    
    for i in range(len(s)-1):
        if s[i] in open:
            if s[i+1] in close:
                return True
            
    return False



def is_valid(s):
    stack=[]
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        else: 
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack)==0

print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True