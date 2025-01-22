li = [10,20,30]
for idx,ele in enumerate(li):
    print(f"Index of {ele} is {idx}")

#WAP To print all Even index element:
for idx, ele in enumerate(li,start=1):
    if idx%2==0:
        print(ele)


