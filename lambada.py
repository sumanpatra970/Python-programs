n=[3,8,6]
sum=lambda n:n*2
print(sum(n))
add=lambda x:(lambda y:x+y)
a=add(20)
b=a(10)
print(b)