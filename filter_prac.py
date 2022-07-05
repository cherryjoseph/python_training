def is_even(x):
    if(x%2 == 0):
        return True
    else:
        return False


arr = list(filter(is_even , [1,2,3,4,5,6,7,8,9,10]))
print(arr)