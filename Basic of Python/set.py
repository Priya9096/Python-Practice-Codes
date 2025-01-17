'''
1.In set we can store Homogeneous as well as Heterogeneous
data.
2.Set is an Unordered Collection of Data.
3.Set does not support indexing of data.
4.In set we cannot store duplicates.
5.Sets are mutable.
'''
s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1)) #{True, 20, 55.44, 10, 'Kodnest'}
#print(s1[0]) #Error

#add():Used to add an element in the set.
s1.add(500)
print(s1)#{True, 'Kodnest', 20, 500, 55.44, 10}

s1.remove(55.44)
print(s1)#{True, 20, 500, 10, 'Kodnest'}

#pop() : Without index will delete and return one ele.
poped_ele = s1.pop()
print(poped_ele)#True
print(s1)#{20, 500, 10, 'Kodnest'}

#del s1[2] #Error
del s1


