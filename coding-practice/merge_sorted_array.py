def merge_sorted_array(nums1, nums2, m, n):
# merge two arrays. last n elements of nums1 and replace with nums2
    cat=m-1
    dog=n-1
    me=m+n-1
    while dog>=0:
        if cat>=0 and nums1[cat]>nums2[dog]:
            nums1[me]=nums1[cat]
            cat-=1
        else:
            nums1[me]=nums2[dog]
            dog-=1
        me-=1
    return nums1
            
    
#we just want the first m to be in the list add in the second array later
def merge_array(nums1, nums2, m, n):
# merge two arrays. last n elements of nums1 and replace with nums2
    for i in range(n):
        nums1[m + i] = nums2[i]
    return nums1

print(merge_sorted_array([1,2,3,0,0],[5,4],3,2))