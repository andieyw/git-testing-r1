def two_sum(nums,target):
    store={}
    for i, num in enumerate(nums):
        pair=target-num
        if pair in store:
            return [store[pair],i] #return as tuple [] vs list ()
        store[num]=i
    return None
print(two_sum([1,2,3,4,5,6],9))
print(two_sum([1,2,3,4],9))