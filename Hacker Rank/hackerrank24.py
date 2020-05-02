def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        var1=oct(i)
        var2=hex(i)
        var3=bin(i)
        print(str(i).rjust(w),var1[2:].rjust(w),"",var2[2:].upper().rjust(w),"",var3[2:].rjust(w))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# def print_formatted(number):
#     width = len('{:b}'.format(number))
#     for i in range(1,number+1):
#         print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)