class parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        print(self.x)
        print(self.y)

class child(parent):
    def __init__(self,t,z,c,d):
        self.t=t
        self.z=z
        super().__init__(c,d)
t1=child(60,80,90,50)
t1.display()

