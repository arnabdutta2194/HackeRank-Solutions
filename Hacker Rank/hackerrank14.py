import re
var=int(input())
arr=list()
for _ in range(var):
    arr.append(input())
# print(arr)
count=0
flag="Invalid"
for i in range(len(arr)):
    if (len(arr[i]) == 10 and arr[i].isalnum()):
        word=arr[i]
        # print(word)
        for j in str(arr[i]):
            if (j.isupper()):    
                count=count+1
        if (count >= 2):
            count=0
            for k in str(arr[i]):
                if (k.isdigit()):
                    count=count+1
            if (count >= 3):
                count=0
                for char in arr[i]:
                    if arr[i].count(char)>1:
                        flag="Invalid"
                        break
                    else:
                        flag="Valid"
                print(flag)
            else:
                print(flag)
        else:
            print(flag)
    else:
        print(flag)
                    


