def myfunc(*args):
    list = []
    for x in args:
        if x%2 == 0:
            list.append(x)
    return list


print(myfunc(3,4,7,9,8))
