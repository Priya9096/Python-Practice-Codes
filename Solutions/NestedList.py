li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])

scores = []
for name, score in li:
    scores.append(score)
scores = list(set(scores))
scores.sort()
second_smallest = scores[1]

names_li =[]
for name, score in li:
    if score == second_smallest:
        names_li.append(name)

names_li.sort()
for name in names_li:
    print(name)
