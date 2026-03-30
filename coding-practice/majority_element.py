def majority_element(nums):
    count={}
    majority=len(nums)/2
    
    for num in nums:
        count[num]=count.get(num,0)+1
        if count[num] > majority:
            return num    

print(majority_element([3,2,3]))        # 3
print(majority_element([2,2,1,1,1,2,2]))# 2
print(majority_element([1]))            # 1