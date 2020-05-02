def swap_case(s):
    z=list()
    for i in  s:
        if i.isupper():
            i=i.lower()
            z.append(i)
        elif i.islower():
            i=i.upper()
            z.append(i)
        else:
            z.append(i)
    x="".join(z)
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    