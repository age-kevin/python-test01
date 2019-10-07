# 转置就是行变列，列变行
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def pringmatrxi(m):
    for ele in m:
        for e in ele:
            print('%2d' % e, end=' ')
        print('')


# 转置函数：第一种写法
# def transformmatrxi(m):
#     # m[0]有几个元素，就代表原矩阵有多少列
#     rt = [[] for i in m[0]]
#     for ele in m:
#         for i in range(len(ele)):
#             # rt[i]代表新矩阵的第i行
#             # ele[i]代表原矩阵当前行的第i列
#             rt[i].append(ele[i])
#     return rt


# 转置函数：第二种写法，用zip函数，zip函数的作用就是把多个序列中的第一个元素合并成新的序列中第一个元素，第二个元素合并成新的序列中第二个元素，以此类推。。。
# 效果：
# [1, 2, 3]  [a, b, c]  [x, y, z]
# #             |
# #             V
# # [1, a, x]  [2, b, y]  [3, c, z]
# def transformmatrxi(m):
#     return list(zip(*m))
#
#


# 转置函数：第三种写法，用numpy的transpose()函数
def transformmatrxi(m):
    import numpy
    return numpy.transpose(m)


pringmatrxi(matrix)

print('=' * 60)

pringmatrxi(transformmatrxi(matrix))


