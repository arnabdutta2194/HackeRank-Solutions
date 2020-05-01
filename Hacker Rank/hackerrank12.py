# var=int(input())
# arr=list()
# for i in range(var):
#     std=input()
#     marks=float(input())
#     arr.append([std,marks])

# arr.sort(key= lambda x: (x[1],x[0]))

# print(arr)
# min=arr[0][1]
# # count=0
# # for i in range(0,len(arr)):

# #     if((arr[i][1]) < min):
# #         min=arr[i][1]
# # print(min)
# # arr.sort(key= lambda x: x[1])
# # for i in range(1,len(arr)):
# #     if(arr[i][1] >= min):
# #         secmin=arr[i][0]
# #         print(secmin)
# #         count=count+1
# #         if(count == 2):
# #             break
# names = [i[0] for i in arr]
# marks = [i[1] for i in arr]
# while marks[0]==min:
#     marks.remove(marks[0])
#     names.remove(names[0])    
# for x in range(0,len(marks)):
#     if marks[x]==min(marks):
#         print(names[x])
N = int(input())

students = []
for i in range(2*N):
    students.append(input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
for k in sorted(result):
    print(k)