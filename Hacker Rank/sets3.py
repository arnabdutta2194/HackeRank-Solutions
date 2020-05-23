var=int(input())
var2=set(map(int,input().split()))
var3=int(input())

for _ in range(var3):
    v=input().split()
    if v[0]=='remove':
        var2.remove(int(v[1]))
    elif v[0] == 'pop':
        var2.pop()
    elif v[0] == 'discard':
        var2.discard(int(v[1]))
    
s=sum(list(var2))
print(s)