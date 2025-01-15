'''In Tuple we can store Homogeneous as well as Heterogeneous Data.
In tuples we can store Duplicates.
Tuples are ordered Collection of Data.
Tuples are Immutable: Once we declare the tuple we cannot modify it.
'''
tup1= (10,22.55,'Kondets',True,10)
print(tup1)#(10, 22.55, 'Kondets', True, 10)
#tup1.remove(55)
#tup1.pop()
#del tup1[2]
print(tup1[2])#'Kodnest'

#Deletes the complete tup1 object
del tup1
#print(tup1)#Error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)#(1, 2, 3, 4, 5, 6)
