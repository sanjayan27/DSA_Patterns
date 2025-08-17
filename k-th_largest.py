def findKthLargest(nums, k):
    # Base case: if list has 1 element, return it
    if len(nums) == 1:
        return nums[0]

    pivot = nums[len(nums) // 2]  # Choose middle element as pivot
    left = [x for x in nums if x > pivot]      # Elements greater than pivot
    middle = [x for x in nums if x == pivot]   # Elements equal to pivot
    right = [x for x in nums if x < pivot]     # Elements smaller than pivot

    # If k is within left, keep searching there
    if k <= len(left):
        return findKthLargest(left, k)
    # If k is within middle
    elif k <= len(left) + len(middle):
        return pivot
    # If k is in right part
    else:
        return findKthLargest(right, k - len(left) - len(middle))

# Example
nums = [8,3,4,6,2,7,9]
k = 2
print(findKthLargest(nums, k))  # Output: 5
