# Definition
def find_max_average(nums: list[int], k: int) -> float:
    """
    Given an integer array nums and an integer k, return the maximum average 
    value of any contiguous subarray of length k.
    """
    
    # fixed length sliding window - length k is given
    # window is window total sum at a point in time
    # max_window to be tracked replace if larger found

    """
    left=0
    right=k
    max_window=0
       
    while right < len(nums):
        window_sum=sum.range(nums[left],nums[right])
        if max_window<window_sum:
            max_window=window_sum
        left+=1
        right+=1
    return max_window/k
    """
    
    window_sum = sum (nums[0:k])
    max_sum=window_sum
    
    for right in range(k,len(nums)):
        window_sum+=nums[right]
        window_sum-=nums[right-k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum/k



# Basic test case
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(find_max_average(nums, k))  # Expected: 12.75