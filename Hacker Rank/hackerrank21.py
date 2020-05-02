var=input()
alnum=alph=dig=islower=isupper=False
for i in var:

    if(i.isalnum()):
        alnum=True
    if(i.isalpha()):
        alph=True
    if(i.isdigit()):
        dig=True
    if(i.islower()):
        islower=True
    if(i.isupper()):
        isupper=True

print(alnum)
print(alph)
print(dig)
print(islower)
print(isupper)