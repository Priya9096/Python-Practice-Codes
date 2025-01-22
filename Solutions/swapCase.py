def swapcase(s):
    sample = ''
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    return sample

res = swapcase('PythoN12')
print(res)




