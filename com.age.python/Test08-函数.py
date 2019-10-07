import random
# def first():
#     print("函数")
#     for i in range(5):
#         print('值：' + repr(i))
#
#
# first()
#
#
# def hello(name):
#     print('你好,' + name)
#
#
# hello('age')


# def test(a):
#     """
#     test函数
#     a - 参数a
#     return - 返回值
#     """
#     print('你好')
#     return a
#
#
# # 查看方法文档
# print(test.__doc__)
# help(test)


# def test():
#     """
#     test - 返回三个大写的随机字符
#
#     """
#     c1 = chr(random.randint(65, 90))
#     c2 = chr(random.randint(65, 90))
#     c3 = chr(random.randint(65, 90))
#
#     return c1, c2, c3
#
#
# r = test()
# print(r)
# a, b, c = test()
# print(a, b, c)


# 计算N的阶乘
# def frac(n):
#     if n < 1:
#         print('n不能小于1')
#         return
#     elif n == 1:
#         return 1
#     else:
#         # n的阶乘总是等于上一个阶乘 * N
#         return frac(n - 1) * n
#
#
# print(frac(3))


# def test(age, height, name='java'):
#     print('name参数为：', name)
#     print('age参数为：', age)
#     print('height参数为：', height)
#
#
# print(test(age=30, height=180))


# def test(num, *books):
#     print('num:', num)
#     print('books:', books)
#
#
# test(24, 'java', 'python', 'C')


# def test(*num, books):
#     print('num:', num)
#     print('books:', books)
#
#
# test(24, 36, 48, 62, books='java')


# def test(*num, books, **scores):
#     print('num:', num)
#     print('books:', books)
#     print('scores:', scores)
#
#
# test(24, 36, 48, 62, books='java', 语文=30, 数学=89)


# def test(a, b):
#     print(a)
#     print(b)
#
#
# ab = ('a', 'b')
# # *对元组自动解包(逆向参数收集)
# test(*ab)
#
# vals = {'a': 89, 'b': 90}
# # 字典解包
# test(**vals)


# name = 'kevin'
# age = 30
#
#
# def testone():
#     sex = 'man'
#     print(name)
#     print(age)
#     print(sex)
#     print(locals())
#
#
# def testtwo():
#     height = 179
#     print(name)
#     print(age)
#     print(height)
#     print(locals())
#
#
# print(globals())
# print('==================================')
# print(locals())
# print('==================================')
# testone()
# print('==================================')
# testtwo()


# name = 'java'
#
#
# def test():
#     name = 'python'
#     print(name)
#
#
# test()
# print(name)


# name = 'java'
#
#
# def test():
#     global name
#     name = 'python'
#     print(name)
#
#
# test()
# print(name)


# def foo():
#     print('foo函数')
#
#     def bar():
#         for i in range(5):
#             print('bar函数')
#     bar()
#
#
# foo()


# def foo():
#     print('foo函数')
#
#     def bar():
#         for i in range(5):
#             print('bar函数')
#     # 返回bar表示返回函数本身（函数也相当于一个值，是function类型的值）、
#     # 返回bar()表示调用函数
#     return bar
#
#
# r = foo()
# print(r)
# r()
# # 这种写法的效果相当于调用完foo()函数返回了bar()函数，然后再调用bar()函数
# foo()()


def test():
    name = 'java'

    def info():
        print('info函数')
        # 声明往后的name变量不是新的局部变量，而是引用所在封闭函数的局部变量
        nonlocal name
        print('name', name)
        name = 'python'
        print('name', name)
    info()
    print(name)


test()

