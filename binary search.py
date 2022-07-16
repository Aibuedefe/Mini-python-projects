# [1,2,3,4,5,6,7,8,9,10]

# Create search function

def search_func(lists,target):
    for items in range(len(lists)):
        if lists[items] == target:
            return items
        
    return -1
    
def binary_search(lists,target, low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lists) - 1
    if high < low:
        return -1
        
    midpoint = (low + high) // 2

    for items in range(len(lists)):
        if lists[midpoint] == target:
            return midpoint
        elif target < lists[midpoint]:
            new_high = midpoint - 1
            return binary_search(lists,target,low,new_high)
        else:
            new_low = midpoint + 1
            return binary_search(lists,target,low,new_low)
        
        
        
lists = [1,2,3,4,5,6,7,8,9,10]
target = 8

print(search_func(lists,target))
print(binary_search(lists,target))