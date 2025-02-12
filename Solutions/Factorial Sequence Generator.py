def factorial_generator(n):
    fact = 1
    for i in range(n + 1):
        if i > 0:
            fact *= i
        yield fact
n = int(input())

for num in factorial_generator(n):
    print(num)
