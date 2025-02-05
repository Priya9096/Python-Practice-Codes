# print('Kodnest1234*'.isalnum()) #False
# print('Kodnest'.isalnum())#True

# print('Kodnest12'.isalpha()) #False
# print('code'.isalpha()) #True

# print('12'.isdigit()) #True

# print('apple'.islower()) #True
# print('apple'.isupper()) #False


# print(any((True,False,False))) #True
# print(any([False,False,False])) #False


#___________LOGIC____________________

s = input() #'qA1'
print(any([i.isalnum() for i in s])) #True
print(any([i.isalpha() for i in s])) #True
print(any([i.isdigit() for i in s])) #True
print(any([i.islower() for i in s])) #True
print(any([i.isupper() for i in s])) #True



