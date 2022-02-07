#program of fliter and map function
nums=[32,12,3,2,21]
x=list(filter(lambda n:n%2==0,nums))
print(x)
y=list(map(lambda n:n*2,x))
print(y)
