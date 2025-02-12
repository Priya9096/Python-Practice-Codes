li = [10,20,30,40]
print(type(li),li)
iterator_object = iter(li)
print(type(iterator_object ),iterator_object)

print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
#print(next(iterator_object)) #StopIteration
