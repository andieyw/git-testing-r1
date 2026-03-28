def reverse_string(s):
    result = ""
    for i in range (len(s) -1, -1, -1):
        result = result + s[i]
        
    return result

print(reverse_string("pie"))
print(reverse_string("1234"))