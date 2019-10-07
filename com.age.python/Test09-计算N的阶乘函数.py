import functools


# 利用循环计算阶乘
# def fract(n):
#     r = 1
#     if n < 1:
#         print('n不能小于1')
#         return
#     else:
#         # i从1循环到n
#         for i in range(1, n + 1):
#             r *= i
#         return r
#
#
# print(fract(6))


# 利用递归计算阶乘
# def fract(n):
#     if n < 1:
#         print('n不能小于1')
#         return
#     elif n == 1:
#         return 1
#     else:
#         return fract(n - 1) * n
#
#
# print(fract(6))

# 利用Python自带的functools.reduce计算
help(functools.reduce)


def fn(x, y):
    return x * y


def fract(n):
    if n < 1:
        print('n不能小于1')
        return
    else:
        # return functools.reduce(fn, range(1, n + 1)) 效果和下面语句效果相同
        # lambda x, y: x * y的本质就是一个函数
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))


print(fract(5))
