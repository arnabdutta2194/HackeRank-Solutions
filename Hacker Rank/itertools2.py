from itertools import combinations

var=input().split()
inp=var[0]
num=int(var[1])
var1=sorted(inp)
var2="".join(var1)
# print(var2)
# print(list)
for i in range(1,num+1):
    for j in combinations(var1,i):
        # print(i)
        str1="".join(j)
        print(str1)
