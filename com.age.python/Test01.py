# import math
# # 转义字符
# s = 'a\tb\tc'
# print(s)
#
# s1 = 'a\nb\nc'
# print(s1)
#
# # 转换说明符：字符串格式化
# s2 = '我爱%s'
# print(s2 % 'Python')
#
# s3 = '我最爱的人是%s，她已经%d岁了'
# print(s3 % ('黄淑恒', 18))
#
# price = 128
# s4 = '价格是%d，八进制为%o，十六进制为%x，字符串形式为%r'
# print(s4 % (price, price, price, price))
#
# # 序列相关的方法
# s5 = 'age.kevin'
# print(s5[4])
# print(s5[2: 6])
# print(s5[2: 6: 3])
# print('ke' in s5)
# print(len(s5))
# print(max(s5))
# print(min(s5))
# print(s5.upper())
# print(s5.lower())
# print(s5.title())
# print(s5.find('eg'))
# print(s5.split('.'))
# print('*'.join(s5.split('.')))
#
# s6 = ' age.kevin '
# print(s6.strip())
# print(s6.lstrip())
# print(s6.rstrip())

# 在idle里面dir(str)可以查看String类型的所有方法，查看其他类方法同理

# # 算术运算符
# div = 5 / 3
# print(div)
#
# div1 = 5 // 3
# print(div1)
#
# mon = 23 % 7
# mon1 = 23 % -7
# mon2 = -23 % -7
# mon3 = -23 % 7
# print(repr(mon)+' '+repr(mon1)+' '+repr(mon2)+' '+repr(mon3))
#
# print(3 ** 3)
#
# print(math.sin(3.14 / 4))

# a = 24
# a -= 10
# print(a)
#
# a *= 4
# print(a)

# 比较运算符

# a = int(input('请输入a:'))
# b = int(input('请输入b:'))
# print(a > b)

# s1 = '213'
# s2 = str(213)
# print(s1 is s2)
# print(s1 == s2)

# 逻辑运算符
# a = 30
# b = 27
# print(3 ** 3 < a and 5 ** 2 > b)
# print(3 ** 3 < a or 5 ** 2 > b)

# 三目运算符

# age = int(input('请输入您的年龄：'))
# print('年龄大于25') if age > 25 else print('年龄小于25')
# print('年龄大于25') if age > 25 else (print('年龄等于25') if age == 25 else print('年龄小于25'))
# s = print('年龄大于25'), '您是一个成年人' if age > 25 else print('年龄小于25')
# print(s)
# s = print('年龄大于25'); '您是一个成年人' if age > 25 else print('年龄小于25')
# print(s)

num = int(input('请输入一个整数：'))
print('十六进制：', hex(num))
print(type(hex(num)))
print('八进制：', oct(num))
print('二进制：', bin(num))
print('十六进制：%X' % num)
print('十六进制：%x' % num)
print('八进制：%o' % num)
