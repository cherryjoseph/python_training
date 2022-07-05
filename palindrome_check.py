def check_palindrome(word):
    rev_word = "".join(list(word)[-1::-1])
    if(rev_word == word):
        print("yes")
    else:
        print("no")    

w = input("enter a word :")
check_palindrome(w)    
