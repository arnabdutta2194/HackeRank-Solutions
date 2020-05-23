var=int(input())
for _ in range(var):
    num_a=int(input())
    set_a=set(map(int,input().split()))
    num_a=int(input())
    set_b=set(map(int,input().split()))
    if set_a.issubset(set_b):
        print('True')
    else:
        print('False')
