var=1
name=list()
for i in range(var+1):
    name.append(input())

def names(fname,lname):
    return f"Hello {fname} {lname}! You just delved into python"

print(names(name[0],name[1]))