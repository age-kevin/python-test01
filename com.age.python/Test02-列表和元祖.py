# my_list = [2, 3, 4, 'python', 6.2, 8]
# my_tuple = (2, 3, 5, 'python')

# my_list1 = list(range(2, 10))
# print(my_list1)

# my_tuple1 = tuple(range(2, 10))
# print(my_tuple1)
#
# list1 = list(my_tuple1)
# print(list1)

# 列表转元祖
# tuple1 = tuple(my_list1)
# print(tuple1)
# print(tuple1[2:5])

# list1 = [20, 'python']
# list2 = list(range(4))
#
# print(list1 + list2)
#
# tuple1 = (20, 'python')
# tuple2 = tuple(range(4))
#
# print(tuple1 + tuple2)
# print(list1 + list(tuple1))

# list1 = ['python', 29, -2]
# print(list1 * 3)
#
# tuple1 = (0, 1, 2, 3)
# print(tuple1 * 3)
#
# s = 'kevin'
# print(s * 5)

# myTuple = 23, 'python', 3.4, 'java'
# print(myTuple)
# print(type(myTuple))

# myList = [23, 'python', 3.4, 'java']
# a, b, *c = myList
# print(a)
# print(b)
# print(c)

myList = ['python', 'java']
myList.append(tuple(range(3, 6)))
myList.extend(range(20, 25))
myList.extend('kotlin')
myList.insert(3, 'C#')
del myList[2]
del myList[4: 6]
myList[2: 4] = ['js']
myList[5: 11] = ['kotlin']
myList.reverse()
print(myList)
print(myList.index('java'))

