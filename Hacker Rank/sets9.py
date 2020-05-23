var=int(input())
st1=set(map(int,input().split()))
l=len(list(st1))

for i in list(st1):
    if list(st1).count(i) == 1:
        capt=i
print(capt)

num_of_group = int(input())
rooms_list = list(input().lstrip().rstrip().split())
rooms_dict = {}
for i in rooms_list:
    if i in rooms_dict:
        rooms_dict[i] += 1
    else:
        rooms_dict[i] = 1
captains_room = [x for x in rooms_dict if rooms_dict[x] == 1]
print(int(captains_room[0]))