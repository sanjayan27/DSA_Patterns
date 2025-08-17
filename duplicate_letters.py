s = "bcabc"
def duplicate(str):
    dict= {}
    arr = list(str)
    for letter in range(0,len(arr)):
        if arr[letter] in dict:
            continue
        else: 
            dict[arr[letter]] = arr[letter] 
            
    return "".join(list(dict.values()))
    
print(duplicate(s))