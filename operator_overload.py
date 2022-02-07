class a:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x+other.y
    def __sub__(self, other):
        return self.x-other.y

    def __mul__(self, other):
        t=self.x
        x=other.y
        t1=t/5
        t2=x/5
        return t1*t2

class b:
    def __init__(self,y):
        self.y=y
t1=a(180)
t2=b(90)
print(t1+t2)
print(t1-t2)
print(t1*t2)
print(t1.__add__(t2))
print(t1.__sub__(t2))
