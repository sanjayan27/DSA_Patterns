nums = [-2,-2,-1,-1,0,1,2,2]
target = 0


def fourSum( nums, target):
    nums.sort()
    result =[]
    for i in range(0,len(nums)-3):
        if nums[i] == nums[i-1] and i > 0:
            continue
        for j in range(i+1,len(nums)-2):
            if nums[j] == nums[j-1] and j > i+1:
                continue
            l = j+1
            r = len(nums)-1 
            while l < r:
                s = nums[i]+nums[j]+nums[l]+nums[r]
                if(s== target):
                    result.append([nums[i],nums[j],nums[l],nums[r]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
                    while nums[r] == nums[r+1] and l < r:
                        r -=1
                elif(s < 0 ):
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
                elif(s>0):
                    r -=1
                    while nums[r] == nums[r+1] and l < r:
                        r -=1

    return result
print(fourSum(nums,target))