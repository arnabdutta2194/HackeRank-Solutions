var1=input()
set1=set(input().split())
var2=input()
set2=set(input().split())

symdiff=set1.symmetric_difference(set2)

lst=list(set(symdiff))
lst=list(map(int,lst))
lst.sort()
for i in lst:
    print(i)
