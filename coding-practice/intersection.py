#list all unique integers that exist in both lists
def intersection(nums1, nums2):
    exists=set(nums1)
    found=set()
 
    for num in nums2:
        if num in exists:
            found.add(num)
    return list(found)
    
    
print(intersection([1,2,2,1], [2,2]))      # [2]
print(intersection([4,9,5], [9,4,9,8,4]))  # [9,4]
print(intersection([1,2,3], [4,5,6]))      # []