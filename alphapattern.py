rows = 5
p = 65
for i in range(rows):
    for j in range(i,rows):
        print(chr(p),end='')
    p=p+1
    print()

q = 64+rows
for i in range(rows):
    for j in range(i,rows):
        print(chr(q),end='')
    q=q-1
    print()