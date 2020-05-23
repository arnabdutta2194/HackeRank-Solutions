var=int(input())
set1=set(map(int,input().split()))
var2=int(input())

for i in range(var2):
    ops=input().split()
    nset=set(map(int,input().split()))
    if ops[0] == 'intersection_update':
        set1.intersection_update(nset)
        # print(set1)
    elif ops[0] == 'update':
        set1.update(nset)
    elif ops[0] == 'symmetric_difference_update':
        set1.symmetric_difference_update(nset)
    else:
        set1.difference_update(nset)

print(sum(list(set1)))