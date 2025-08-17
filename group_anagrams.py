value = ["abc","acb","ate"]
def anagrams(arr):
    dict = {}
    for word in arr:
        sorted_words = "".join(sorted(word))
        if sorted_words in dict:
            dict[sorted_words].append(word)
        else:
            dict[sorted_words] = [word]
        
        
    return list(dict.values())
print(anagrams(value))

