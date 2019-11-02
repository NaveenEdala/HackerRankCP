if __name__ == '__main__':
    s = input()
    a = b = c = d = e = False
    for i in s:
        if a != True: 
            a = i.isalnum()
        if b != True:
            b = i.isalpha()
        if c != True:
            c = i.isdigit()
        if d != True:
            d = i.islower()
        if e != True:
            e = i.isupper()
    print(str(a))
    print(str(b))
    print(str(c))
    print(str(d))
    print(str(e))
