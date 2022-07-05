def do_fact(num,lvl):
    temp_num = num
    res = 1
    while (lvl>0):
        res = res * temp_num
        temp_num = temp_num -1
        lvl = lvl -1
    return res


my_num = int(input("enter a number :"))
my_lvl = int(input("enter a level :"))

result = do_fact(num=my_num , lvl=my_lvl)
print(f"result is :{result}")
