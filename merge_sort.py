arr = [3,5,2]

def merge(arr):

    if(len(arr)>1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        
        merge(left)
        merge(right)

        left_point = 0
        right_point = 0
        final_point = 0
        
        while left_point < len(left) and right_point < len(right):
            if left[left_point] < right[right_point]:
                arr[final_point] = left[left_point]
                left_point += 1
                
            else:
                arr[final_point] = right[right_point]
                right_point = right_point + 1
                
            final_point +=1
        
        while left_point < len(left):
            arr[final_point] = left[left_point]
            left_point+=1
            final_point +=1 
            
        while right_point < len(right):
            arr[final_point] = right[right_point]
            right_point +=1 
            final_point +=1 
merge(arr)
print(arr)