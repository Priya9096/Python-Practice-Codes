li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]

#When we have only if part then write it after for loop.
even = [i for i in li1 if i%2 == 0]
sq_list = [i**2 for i in li1]
new_li1 = [ele+2 for ele in li1]

#When we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li1 ]

#Multiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]




