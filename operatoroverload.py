#program of operator overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=student(m1,m2)
        return m3
    def display(self):
        print(self.m1)
        print(self.m2)

s1=student(32,76)
s2=student(98,87)
s3=s1+s2
s3.display()
