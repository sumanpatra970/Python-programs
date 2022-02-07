#program to know leapyear
def leap(year):
    x=year/4
    if x==0:
        print("leap year")
    else:
        print("not a leap year")
yr=int(input("ener year"))
leap(yr)