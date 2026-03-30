def two_sum(nums, target):
    store={}
    
    for i, num in enumerate(nums):
        if not isinstance(num, (int, float)): #skip non-int + float
            continue
        
        match=target-num # match=3 (5-2)
        if match in store:
            return[store[match],i] #store[match] --> gets me the array index

        store[num]=i

    
print(two_sum([2,1,0,3],5)) #[0,3]
print(two_sum([2,1,-2,3],0)) #[0,2]
print(two_sum([2,2,-2,3],0)) #[0,2]
print(two_sum([1,2,3,3],5)) #[1,2]
print(two_sum(["a",2,3,3],5)) #[1,2]
print(two_sum([True,2,3,3],5)) #[1,2]