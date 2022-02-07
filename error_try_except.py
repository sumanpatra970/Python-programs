#program of exception handling
a=int(input("enter no"))
b=int(input("enter no"))
try:
    print("resource opened")
    print(a/b)
except ZeroDivisionError as e:
    print("hey you can not divide by zero",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something wrong")
finally:
    print("resource closed")

