def sort(arr):
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1] 

arr= [1,2,3,4]
sort(arr)
print(arr)