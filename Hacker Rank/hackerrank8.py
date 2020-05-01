# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

def arrfunc():
    if (s[0] == 'insert'):
        arr.insert(int(s[1]),int(s[2]))
    elif (s[0] == 'print'):
        print(arr)
    elif (s[0] == 'remove'):
        arr.remove(int(s[1]))
    elif (s[0] == 'append'):
        arr.append(int(s[1]))
    elif (s[0] == 'sort'):
        arr.sort()
    elif (s[0] == 'pop'):
        arr.pop()
    elif (s[0] == 'reverse'):
        arr.reverse()

var = int(input())
arr=list()
for val in range(var):
    s=input().split()
    arrfunc()