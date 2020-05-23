from itertools import permutations

var=input().split()
inp=var[0]
num=int(var[1])
var1=sorted(inp)
var2="".join(var1)
perm = permutations(var2,num)
for i in list(perm):
    str1="".join(i)
    print(str1)
