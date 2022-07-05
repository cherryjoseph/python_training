def is_palindrome(s):
    if(s == s[-1::-1]):
        print("True")
    else:
        print("No. Not palindrome") 

def sum_digits(num):
    sum =0
    for i in list(str(num)):
        sum = sum + int(i)
    return sum 
        

