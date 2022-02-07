#program of class inheritance
class a:
    def __init__(self,mark):
        self.mark=mark
        print(mark)
    def grade(self, mark):
        if mark>90:
            print("grade a")
        elif mark>80:
            print("grade b")
        else:
            print("fail")
class b(a):
    def __init__(self, agenew, marknew):
        super().__init__(marknew)
        self.agenew=agenew
        print("age is=",agenew)
    def old(self,agenew):
        if agenew>80:
            print("older one")
        else:
            print("young one")
age=int(input("enter age"))
mark=int(input("enter mark"))
a1=b(age,mark)
a1.grade(70)
