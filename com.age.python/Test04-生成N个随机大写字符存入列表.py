# import random
import numpy

NUM = 10

# 传统方式
# result = []
# for i in range(NUM):
#     # 生成65到90的随机数
#     n = random.randint(65, 91)
#     result.append(chr(n))
#
# print(result)

# 列表推导式
# result = [chr(random.randint(65, 90)) for i in range(NUM)]
# print(result)

# 使用numpy模块一次生成N个随机数，生成一个矩阵，相当于一个包含NUM个随机数的列表
result = [chr(i) for i in numpy.random.randint(65, 90, [NUM, 1])]

print(result)

