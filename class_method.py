#program to show class method
class car:
    wheel=5
    def __init__(self,name,model):
        self.name=name
        self.model=model
    @classmethod
    def info(cls):
        cls.wheel=6
c1=car("navin",24)
c2=car("suman",22)
car.info()
print(c1.name)
print(c2.model)
print(car.wheel)