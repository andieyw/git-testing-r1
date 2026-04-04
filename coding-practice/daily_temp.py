def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Given a list of daily temperatures, return a list such that:
    for each day, tells you how many days you have to wait until a warmer temperature.

    If there is no future day with a warmer temperature, put 0 instead.
    """
    
    n = len(temperatures) # we care about day n (index 2 is day 3) not index eg [Day 1, Day 2, Day 3] but index [0, 1, 2]
    # result is list we will return
    # list with value 0 n times ie  if n=5  [0, 0, 0, 0, 0] --> there is one result per index
    result = [0]*n 
    stack=[] #store indices
    
    for i in range(n):
        # "stack" --> check stack is not empty
        # "temperatures[stack[-1]]" --> temp of top day in stack
        # "temperatures[i] > temperatures[stack[-1]]" --> check that current day [i] is warmer than top day in stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # while current day is the warmest day keep popping (resolving) the top store
            prev=stack.pop()
            result[prev]=i-prev
        # if not warmer add current day index to stacks
        stack.append(i)
        
    return result


# Basic test case
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temps))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]