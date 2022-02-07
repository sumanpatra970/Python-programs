#program of class inheritance
class A:
    def __init__(self):
        print("in constructor of class a")
    def fun1(self):
        print("in fun1")
    def fun2(self):
        print("in fun2")
class B(A):
    def __init__(self):
        super().__init__()
        print("in constr in class b")
    def fun3(self):
        print("in fun3")
    def fun4(self):
        print("in fun4")
a1=B()
a1.fun1()
a1.fun2()