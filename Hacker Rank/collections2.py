x= 0;k = int(input())
m = input().strip().split()
for i in range(k): x = x+int(input().split()[m.index('MARKS')])
print(float(x)/k)