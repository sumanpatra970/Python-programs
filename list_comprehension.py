number=[2,7,6,5]
number_square=[num*2 for num in number]
print(number_square)
friends=['Rolf','Ket','Watson']
friend=input("enter your friend name")
friends_lower=[frnd.lower() for frnd in friends]
print(friends_lower)
frnd_lowerr=friend.lower()
print(frnd_lowerr)
for name in friends_lower:
    print(name,frnd_lowerr)
    if name == frnd_lowerr:
        print("ket is my friend")
    else:
        print("no friend is found",name,frnd_lowerr)