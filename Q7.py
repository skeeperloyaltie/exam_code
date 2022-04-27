# Write a recursive function F(n) that takes a non-empty string n as input 
# and returns a string after removing the consecutive duplicates from n. If any 
# character in the string has a multiple consecutive occurences, you need to keep exactly one 
# occurence.



def F(n):
    
    n = ""
    if len(n) == 1:
        return n
    else:
        if n[0] == n[1]:
            return F(n[1:])
        else:
            return n[0] + F(n[1:])
        
def main():
    print(F("afbcxa"))
    
if __name__ == "__main__":
    main()