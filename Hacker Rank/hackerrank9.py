var1=int(input())
var2=input()

vals=var2.split(" ")
print(vals)
tup=()

for i in range(var1):
    tup = tup + (int(vals[i]),)

print(hash(tup))