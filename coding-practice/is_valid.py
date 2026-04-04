def is_valid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    A string is valid if:
    - Open brackets are closed by the same type of brackets
    - Open brackets are closed in the correct order
    """
    
    stack = []
    # be careful with mapping and what is key vs value
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        # check if char is a opening bracket
        if char in mapping.values():
            stack.append(char)
        else:
            # if char is closing bracket check if stack is empty 
            # or
            # check if the top of the stack ( stack[-1] ) ie last opening bracket  IS NOT   the key to the closing bracket eg {"(_: ")"}
            # return false i one of the above contions is met
            # otherwise the char is the corresponding closing bracket. we mark as valid and pop the stack[-1] as the matching bracket has been found. move onto next char
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()    
    
    #check that stack is empty and that we can say we have checked all char in s and thus entire s is valid
    return len(stack)==0    


# Basic test cases
print(is_valid("()"))        # Expected: True
print(is_valid("()[]{}"))    # Expected: True
print(is_valid("(]"))        # Expected: False
print(is_valid("([)]"))      # Expected: False
print(is_valid("{[]}"))      # Expected: True