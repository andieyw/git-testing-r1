def incorrect_sorted(numbers, target):
    pointer1 = 0
    pointer2 = 1
    for i, num in enumerate(numbers):
        numbers[i]
        if numbers[pointer1]+numbers[i]== target:
            return list[pointer1,i]
        i+=1
        
        
        
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers)-1
    
    while left < right:
        current = numbers[left]+ numbers[right]
        
        if current == target:
            return [left+1, right +1]
        elif current < target:
            left +=1
        else:
            right-=1



print(two_sum_sorted([2,7,11,15], 9))   # [1,2]
print(two_sum_sorted([2,3,4], 6))       # [1,3]
print(two_sum_sorted([-1,0], -1))       # [1,2]