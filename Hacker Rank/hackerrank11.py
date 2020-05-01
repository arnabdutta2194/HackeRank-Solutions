# Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

var1=int(input())
var2=input()

var2=var2.split(" ")
arr=list()
for val in range(0,var1):
    arr.append(int(var2[val]))

arr.sort()
arr.reverse()

max=arr[0]

for val in range(len(arr)):
    if arr[val] < max:
        print(arr[val])
        break
    