li1 = list('Kod')
print(li1) #['K', 'o', 'd']

li2 = list((10,20))
print(li2) #[10, 20]

li3 = list({100,200})
print(li3) #[200, 100]

li4 = list({'Name':'Priya','age':22})
print(li4) #['Name', 'age']

li5 = list(range(1,11))
print(li5)

#tuple(iterable_object)
tup1 = tuple([10,20,30])
print(tup1) #(10, 20, 30)
tup2 = tuple({100,200})
print(tup2) #(200, 100)
tup3 = tuple(range(1,11))
print(tup3)#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup4 = tuple('Kodnest')
print(tup4) #('K', 'o', 'd', 'n', 'e', 's', 't')
tup5 = tuple({'name':'Priya','age':22})
print(tup5) #('name', 'age')

#set(iterable_object):
s1 = set([10,20,20,30])
print(s1) #{10, 20, 30}

#dict(iterable_object:key:value)
d1 = dict([['name','Priya'],['age',22]])
print(d1) # {'name': 'Priya', 'age': 22}
