import itertools
import random

myList = [random.randint(20, 30) for i in range(15)]
print(myList)

# 一、新列表收集法，只收集不重复的元素
# myNewList = []
#
# for ele in myList:
#     if ele not in myNewList:
#         myNewList.append(ele)
#
# print(myNewList)

# 二、将原列表传给set集合，自动去重
# myNewList = list(set(myList))
# print(myNewList)

# 三、利用分组队列表进行去重，原理是相同的元素就分成一组，那么不同的元素就是不同的组，但是注意分组前列表要排序
myList.sort()

it = itertools.groupby(myList)

for k, g in it:
    print(k, end=" ")
