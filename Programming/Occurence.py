li = list(map(int,input().split())) #[10,20,20,30]
d =  {}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for num, count in d.items():
    print(f"{num} occures {count} time(s)")
