numbers = [1,2,4,6]
target = 6

l = 0
r = len(numbers)-1
while l < r:
    acc = numbers[l] + numbers[r]
    if acc == target:
        print(l,r)
        break
        
    elif acc < target:
        l= l + 1
    elif acc>target :
        r = r+1
    