var=int(input())
std1=set(map(int,input().split()))
var2=int(input())
std2=set(map(int,input().split()))

std=std1.difference(std2)
print(len(list(std)))