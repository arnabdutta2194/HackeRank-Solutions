from collections import deque
var=int(input())
dq=deque()
for i in range(var):
    inp=input().split()
    op=inp[0]
    try:
        num=inp[1]
    except:
        pass
    if op == "append":
        dq.append(int(num))
    elif op == "appendleft":
        dq.appendleft(int(num))
    elif op == "pop":
        dq.pop()
    elif op == "popleft":
        dq.popleft()
        
for i in dq:
    print(i, end=" ")