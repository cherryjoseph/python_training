def square_val(val):
    return val**2

arr = [1,2,3,4]
square_arr = list(map(square_val , arr))
print(square_arr)