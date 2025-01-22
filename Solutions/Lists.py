li = []
n = int(input())
for i in range(n):
    command,*values = input().split()
    values = list(map(int,values))
    if (command == 'insert'):
        li.insert(values[0],values[1])
    if (command == 'print'):
        print(li)
    if (command == 'remove'):
        li.remove(values[0])
    if (command == 'append'):
        li.append(values[0])
    if (command == 'sort'):
        li.sort()
    if (command == 'pop'):
        li.pop()
    if (command == 'reverse'):
        li.reverse()

