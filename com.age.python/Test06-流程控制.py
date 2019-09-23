"""

    if分支的三种语法格式：

        if 条件:
            执行体
------------------------
        if 条件:
            执行体1
        elif 条件:
            执行体2
        elif 条件：
            执行体2
        ...
        else:
            执行体3

"""

# age = int(input("请输入您的年龄:"))
#
# if age > 25:
#     print('您的年龄大于25')
# else:
#     print('您的年龄小于25')

# score = int(input('您的成绩是：'))
#
# if score > 90:
#     print('优秀')
# elif score > 80:
#     print('良好')
# elif score > 70:
#     print('中等')
# elif score > 60:
#     print('及格')
# else:
#     print('去死吧')

# s = 'fkjava'
# if s:
#     print('s不是空')
#
# # 所有代表空的值，如0,'',[],(),{},None都会被当成False处理
# s2 = ''
# if s2:
#     print('s2不是空')

# age = int(input('请输入您的年龄：'))

# 这种写法代替Java中的三目运算符
# print('您的年龄大于25') if age > 25 else (print('您的年龄小于25') if age < 25 else print('您的年龄等于25'))

# if age > 25:
#     # 空语句：啥也不干
#     pass
# else:
#     print('啥都干')

# myList = ['java', 'python', 'js', 'kotlin']
#
# i = 0
# while i < len(myList):
#     print(myList[i])
#     i += 1

# myData = {'java': 59, 'python': 60, 'kotlin': 50, 'js': 30}
#
# i = 0
#
# # 将字典所有的key转换成List
# keyList = list(myData.keys())
# while i < len(keyList):
#     print(keyList[i], myData[keyList[i]])
#     i += 1

# for-in循环遍历字符串

s = 'python'
# s(序列)有几个元素，for-in循环就重复几次，循环计数器就自动、依次等于每个元素
for c in s:
    print(c)

myTuple = (20, 30, 40, 50)
for i in myTuple:
    print(i)

myData = {'java': 59, 'python': 60, 'kotlin': 50, 'js': 30}
for key in myData.keys():
    print(key)

for key, value in myData.items():
    print(key, value)
