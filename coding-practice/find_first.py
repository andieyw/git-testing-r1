# Definition
def find_first(nums: list[int], target: int) -> int:
    """
    Given a sorted array nums (ascending), return the index of the first occurrence
    of target. If target does not exist, return -1.
    """
    
    # binary search with left boundary
    # left + right//2 mid
    # if mid==target
    # right = mid -1
    
    left=0
    right=len(nums)-1
    answer=-1
    
    while left<=right:
        mid = (left+right)//2
        if nums[mid] == target:
            answer=mid
            right=mid-1
        elif nums[mid] <= target:
            left = mid+1
        else:
            right = mid-1
    return answer

# Basic test cases
print(find_first([1, 2, 2, 2, 3, 4], 2))  # Expected: 1
print(find_first([1, 2, 3, 4, 5], 3))     # Expected: 2
print(find_first([1, 1, 1, 1], 1))        # Expected: 0
print(find_first([1, 2, 3, 4], 6))        # Expected: -1