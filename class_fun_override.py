#program of function override
class parent:
    def info(self):
        print("my prent mobile is nokia 1100")
class child(parent):
    def info(self):
        print("my own mobile is sam a1")
a1=child()
a1.info()