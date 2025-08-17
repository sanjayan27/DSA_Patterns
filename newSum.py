def maximum69Number (num):
    num = str(num)
    string = list(num)
    for i in range(0,len(string)):
        if string[i] == 9:
            continue
        elif string[i] == "6":
            string[i] = "9"
            num = int("".join(string))
            return num
        
print(maximum69Number(9969))



