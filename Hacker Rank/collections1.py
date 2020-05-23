from collections import Counter
num_of_shoes=int(input())
shoe_sizes=list(map(int,input().split()))
shoe_sizes_counter=Counter(shoe_sizes)
# print(shoe_sizes_counter.items())

num_of_cus=int(input())
total_sum=0

for _ in range(0,num_of_cus):
    lst=input().split()
    size=int(lst[0])
    price=int(lst[1])
    # print(size,price)
    # print(shoe_sizes_counter[size])
    if shoe_sizes_counter[size] != 0:
        # print("Here")
        total_sum=total_sum+price
        shoe_sizes_counter[size]=shoe_sizes_counter[size]-1
        print(shoe_sizes_counter[size])

print(total_sum)