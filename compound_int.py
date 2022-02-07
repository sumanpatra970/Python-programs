#program to calculate compound interest
principal=int(input("enter principal amount"))
time=int(input("enter time"))
rate=int(input("enter rate"))
ci=principal*pow((1+rate/100),time)-principal
print("compound interest is=",ci)