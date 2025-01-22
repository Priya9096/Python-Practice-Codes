def mutate_string(string, position, character):
    li = list(string)
    li[position]=character
    string = "".join(li)
    return string

s = input()
p, c = input().split()
res = mutate_string(s, int(p),c)
print(res)
            