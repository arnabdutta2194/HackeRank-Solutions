n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum=0
marks=student_marks[query_name]
for i in range(len(marks)):
    sum=sum + marks[i]
print("{:.2f}".format(sum/len(marks)))
