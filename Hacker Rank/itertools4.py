from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
prod=product(a,b)
z=list(prod)
for i,j in z:
    print((i,j),end=" ")