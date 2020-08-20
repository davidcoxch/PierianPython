def ran_check(num,low,high):
    if num in range(low,high+1):
        print("{} is between {} and {}".format(num,low,high))
        


ran_check(5,2,7)


def ran_bool(num,low,high):
    return  num in range(low,high+1)

print(ran_bool(3,1,10))