

s = "A man, a plan, a canal: Panama"
reverse = ""
for char in s:
    if char.isalnum():
        reverse+=char

d= reverse.lower()
val = d[::-1]
if d == val:
    print(True)
else:
    print(False)