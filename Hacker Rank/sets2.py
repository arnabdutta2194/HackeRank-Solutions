var=int(input())
s=list()
for _ in range(var):
    var1=input()
    s.append(var1)

st=set()
for i in s:
    st.add(i)
print(len(st))