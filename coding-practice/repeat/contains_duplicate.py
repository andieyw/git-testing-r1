def wrong_contains_duplicate(nums):
    seen=[]
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.append(nums[i])
            i+=1
        return False

    return True

def list_contains_duplicate(nums):
    seen = []
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False
print(contains_duplicate([0,0,1])) # True