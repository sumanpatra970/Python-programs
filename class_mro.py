#program MRO
class A:
    def __init__(self):
        print("in constructor1")
    def fun1(self):
        print("in fun1")
    def fun2(self):
        print("in fun2")
class B:
    def __init__(self):
        print("in constructor2")
    def fun3(self):
        print("in fun3")
    def fun4(self):
        print("in fun4")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in constructor3")
    def fun5(self):
        print("in fun 5")
c1=C()
c1.fun3()
c1.fun2()