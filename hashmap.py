# class MyHashMap:

#     def __init__(self):
#         self.size = 10**6 +1 
#         self.arr = [-1] * self.size

#     def getIndex(self,key:int):
#         index = hash(key) % self.size
#         return index

#     def put(self, key: int, value: int) -> None:
#         index = self.getIndex(key)
#         self.arr[index] = [[key,value]]
        
#     def get(self,key:int) ->None:
#         index= self.getIndex(key)
#         if self.arr[index] != -1:
#             for i in self.arr[index]:
#                 if key == i[0]:
#                     return 1
#         return -1
#     def remove(self,key:int) -> None:
        
            
    
    
# dicts = MyHashMap() 
# dicts.put("name","sanjay")
# print(dicts.get("names"))