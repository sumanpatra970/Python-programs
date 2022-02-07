#program to swap two element in list
def list():
    id=[2,8,9,7]
    n=len(id)
    t=id[0]
    id[0]=id[n-1]
    id[n-1]=t
    print(id)
list()