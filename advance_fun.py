number=[2,4,5,6]
def ready(i):
    if i%2==0:
        return True
    else:
        return False

pro=list(filter(ready,number))
print(pro)

pro_no=list(filter(lambda x:x%2,number))
print(pro_no)

pro_num=list(map(lambda y:y*3,number))
print(pro_num)