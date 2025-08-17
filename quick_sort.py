import random


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr)
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
    
    
arr = [3,1,5,2]
print(quick_sort(arr))