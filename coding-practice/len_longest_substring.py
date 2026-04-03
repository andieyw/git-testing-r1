# Definition
def length_of_longest_substring(s: str) -> int:
    """
    Given a string s, return the length of the longest substring 
    without repeating characters.
    A substring is a contiguous sequence of characters.
    """
    # longest --> variable window
    # assume that the repeating is for any index location eg a repeats at 0 and 4 counts
    # we would need a window - left + right pointer
    # we would need a counter for length
    # window is invalid is an element within appears more than once
    # use set as we just need to check if it exists
    
    left=0
    seen=set()
    max_length=0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length

# Basic test case
s = "abcabcbb"
print(length_of_longest_substring(s))  # Expected: 3