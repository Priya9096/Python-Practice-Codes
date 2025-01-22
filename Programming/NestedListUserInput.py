li = list(map(int,input().split()))
i =int(input())
if (i in li):
        print(f"The index of {i} in the tuple is: {li.index(i)}")
else:
        print(f"{i} is not in the tuple.")


# li = []
# sub_list_count = int(input())
# for i in range(sub_list_count):
#     sub_li = list(map(int,input('Enter sublist ele').split()))
#     li.append(sub_li)
# print(li)

'''
3
Enter sublist ele100 200
Enter sublist ele10 30 40
Enter sublist ele30
[[100, 200], [10, 30, 40], [30]]
'''




