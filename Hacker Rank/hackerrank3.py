# Task
# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

var1= int(input())
var2=int(input())

def add(var1,var2):
    return var1+var2
def diff(var1,var2):
    if (var1>var2):
        return var1-var2
    else:
        return var2-var1
def prod(var1,var2):
    return (var1*var2)

sum=add(var1,var2)
differ=diff(var1,var2)
prduct=prod(var1,var2)

print(sum)
print(differ)
print(prduct)
