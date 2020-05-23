# set_a=list(map(int,input().split()))
# var=int(input())
# sub="True"
# count=0
# while count<var:
#     sub_set=list(map(int,input().split()))
#     for i in sub_set:
#         if len(set_a) == len(sub_set):
#             sub = "False"
#             break
#         elif i in set_a:
#             sub="True"
#         else:
#             sub="False"
#             break
#     count+=1

# print(sub)

A = set(map(int,input().split()))
b = int(input())
ans = True
for _ in range(b):
    tmp = set(map(int,input().split()))
    if not (len(A) > len(A & tmp) and len(tmp - A) == 0):
        ans = False
        break
print ans