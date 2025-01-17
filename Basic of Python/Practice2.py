li1 = list(range(1,10))
print(li1)

tup1 = tuple(range(1,10))
print(tup1)

s1 = set(range(1,10))
print(s1)

d1 = dict([('one',1)])
print(d1)


# in_str= input('Enter key:value key:value')
# d2 = {key: int(value) for key,value in (i.split(':') for i in in_str.split())}
# print(d2)

li1 = [[1,2],[3,4]]
li2= [ele if ele%2==0 else 'no' for i in li1 if len(i)>2 for ele in i]
print(li2)


