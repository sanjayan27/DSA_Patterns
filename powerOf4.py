n = 64
def power4(n):
    if n <= 0:
        return -1
    while n % 4 == 0:
        n //=4
    
    return n==1

print(power4(n))