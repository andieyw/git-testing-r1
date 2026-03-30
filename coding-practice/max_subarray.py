def incorrenct_max_subarray(nums):
    for i in range(len(nums)-1):
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1]:
            if current_sum > max_sum:
                max_sum=current_sum(nums[i])
                i+=1
    return max_sum

def max_subarray(nums):
    current_sum=nums[0]
    max_sum=nums[0]
    
    for num in nums[1:]:
        current_sum=max(num, current_sum+num)
        max_sum=max(max_sum,current_sum)
        
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(max_subarray([1])) # 1
print(max_subarray([5,4,-1,7,8])) # 23