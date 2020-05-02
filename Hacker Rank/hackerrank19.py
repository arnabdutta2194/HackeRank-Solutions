#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # string=s.split()
    # for i in range(len(string)):
    #     b=list()
    #     a=string[i]
    #     if (a[0].islower()):
    #         c=a[0].upper()
    #         d=c+a[1:]
    #         b.append(d)
    #         string.remove(a)
    #         string.insert(i,d)
    #     else:
    #         pass
    # str1=""
    # for i in string:
    #     str1+=i
    # return(str1)
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)


    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
