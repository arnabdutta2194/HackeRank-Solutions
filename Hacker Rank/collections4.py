# from collections import defaultdict

# var = input().split()
# a=var[0]
# b=var[1]

# a_dict=defaultdict(list)
# b_dict=defaultdict(list)

# for i in range(1,int(a)+int(b)+1):
#     var=input()
#     if var == 'a':
#         a_dict[var].append(i)
#     elif var == 'b' or var != 'b':
#         if var == 'b':
#             b_dict[var].append(i)
#         else:
#             b_dict['b'].append(-1)


# for i in a_dict['a']:
#     print(i,end=" ")
# for i in b_dict['b']:
#     print(i,end=" ")    
from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i]) ))
    else:
        print(-1)