# map(function, iterable_object) ---> Iterator Object

def double(x):
    return x*2

li = [1,2,3,4]
double_li = list(map(double,li))
print(double_li) #[2, 4, 6, 8]

tup = ('10','20','30')
print(tup) #('10', '20', '30')
tup = tuple(map(int,tup))
print(tup) #(10, 20, 30)

li2 = [1,5,66]
print(li2)
li2 = list(map(float,li2)) 
print(li2) #[1.0, 5.0, 66.0]


