def palindrom_check():
    w = input("enter a word :")
    if(w[::-1]==w):
        print("yes")
    else:
        print("no")

palindrom_check()