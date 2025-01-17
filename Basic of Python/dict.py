#dict is Mutable.
d1 = {'name':'Priya','age':27,'phone':23456,'age':29}
print(d1,type(d1))#{'name': 'Priya', 'age': 29, 'phone': 23456}

#In dict we cannot store duplicate keys.
d1['name']= 'Pooja'
print(d1)#{'name': 'Pooja', 'age': 27, 'phone': 23456}

#In dict we can store duplicate values.
marks = {'Sci':85,'Maths':85} #Allowed

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)

#list(),tuple(),set(),dict()


#int(), float(), str(), bool(), complex()