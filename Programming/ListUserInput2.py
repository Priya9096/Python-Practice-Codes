# li = input('Enter space seperated Elements') #10 20
# print(li, type(li)) #'10 20' <class 'str'>
# li = li.split()
# print(li) #['10', '20']
# li = list(map(int,li))
# print(li) #[10, 20]


# tup = tuple(map(int,input('Enter Space seperated Elements ').split()))
# print(tup)

li = list(map(int,input().split()))
print([i for i in li if i%2 == 0])



