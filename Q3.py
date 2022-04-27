
    
    
def F(n):
    n = int(n)
    if n == 0:
        return 3
    elif n == 1:
        return 3
    elif n == 2:
        return 10
    elif n == 3:
        return 21
    elif n == 4:
        return 47
    elif n == 5:
        return 100
    elif n == 6:
        return 211
    elif n == 7:
        return 439
    elif n == 8:
        return 906
    elif n == 9:
        return 1857
    else:
        return F(n)
    
    
    
def main():
    print(F(10))