

def f(s):
    odd = ""
    even = ""
    for i in s:
        if i.isdigit():
            if int(i) % 2 == 0:
                even += i
            else:
                odd += i
    return even + odd


def main():
    print(f("a1b2c3d4e5f6g7h8i9j0"))
    print(f("a1b2c3d4e5f6g7h8i9j0k"))
    print(f("a1b2c3d4e5f6g7h8i9j0k1"))
    print(f("a1b2c3d4e5f6g7h8i9j0k1l"))
    print(f("a1b2c3d4e5f6g7h8i9j0k1l2"))
    print(f("a1b2c3d4e5f6g7h8i9j0k1l2m"))
    print(f("a1b2c3d4e5f6g7h8i9j0k1l2m3"))
    
if __name__ == "__main__":
    main()