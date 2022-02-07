#program to check pallindrome
def pallindrome():
    str =input("enter string")
    newstr = ""
    n = len(str)
    for i in range(n, 0, -1):
        newstr = newstr + str[i - 1]
        print(newstr)
    if str==newstr:
        print("palindrome")
    else:
        print("not a pallindrome")
pallindrome()