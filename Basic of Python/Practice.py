'''
1.reverse, reversed
2.sort(), sorted()
3.map
4.list input: Different Ways: Normal for loop,split and map
5.Nested List Input and Unpacking nested lists 
6.Hackerank que: Find Runner-up score
7.Hackerank Que: Nested List
8.Practice and Homeworks
9.enumerate()
10. * operator
'''
#Pack multiple arguments into a single parameter as a tuple.
def disp(*args):
    print(args)
disp(10,20,30)

#Unpacks a list (or any iterable) into separate arguments.
def add(a,b,c):
    print(a,b,c)
add(*[10,20,30])

#Unpack part of a list into a variable.
li = ['Krishna',10,20,30,40,'Patil']
fname, *scores , lname = li
print(fname, scores , lname )
