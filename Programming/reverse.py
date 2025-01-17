#object.reverse() will reverse the original object.
li = [10,5,20,7,40]
print('Before Reverse:',li)
li.reverse()
print('After Reverse:',li) #[40, 7, 20, 5, 10]

#list(reversed(object)):
li2 = [11,6,8,22]
reverse_li2=list(reversed(li2))
print(li2)#[11, 6, 8, 22]
print(reverse_li2)#22, 8, 6, 11]

li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3)) #-->Creating new reverse list
li3.reverse() #--->Reversing Original List