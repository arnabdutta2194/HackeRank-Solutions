def split_and_join(line):
    linesp=line.split()
    linesp="-".join(linesp)
    return linesp


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)