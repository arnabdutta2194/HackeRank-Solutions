from collections import OrderedDict,defaultdict
def_dict=defaultdict(list)
items_dict=OrderedDict()
items=int(input())

for _ in range(items):
    k=input().split()
    k[0]=' '.join(k[0:len(k)-1])
    k[1]=int(k[len(k)-1])
    k=k[0:2]
    def_dict[k[0]].append(k[1])
    items_dict[k[0]]= _

for i in items_dict:
    print(i,sum(def_dict[i]))