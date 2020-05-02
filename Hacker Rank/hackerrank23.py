# Given an integer, n, perform the following conditional actions:

# If  n is odd, print Weird
# If  n is even and in the inclusive range of  2 to 5, print Not Weird
# If  n is even and in the inclusive range of  6 to 20 , print Weird
# If  n is even and greater than 20 , print Not Weird

var=int(input())


if var%2 != 0 :
    print("Weird")
elif var%2 == 0  and (var in range(2,5+1)):
    print("Not Weird")
elif var%2 == 0 and (var in range(6,20+1)):
    print("Weird")
elif var%2 == 0 and var>20:
    print("Not Weird")

