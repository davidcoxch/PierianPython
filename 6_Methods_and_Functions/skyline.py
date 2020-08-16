def myfunc(a):
    res=''
    for s in range(len(a)):
        if s%2 == 0:
            res = res + a[s].upper()
        else:
            res = res + a[s].lower()
    return res




print(myfunc('hello'))