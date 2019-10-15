# scores = {'语文': 85, '数学': 90, '英语': 30}
# print(scores)

# scores = dict([('语文', 85), ('数学', 90), ('英语', 30)])
# print(scores)
#
# scores = dict(语文=85, 数学=90, 英语=30)
# print(scores)
# print(scores['语文'])
# scores['生物'] = 80
# print(scores)
# scores['数学'] = 95
# print(scores)
# del scores['英语']
# print(scores)
# print('数学' in scores)

# scores.update({'语文': 89, '生物': 91})
# print(scores)
#
# for key in scores.keys():
#     print(key)
#
# for value in scores.values():
#     print(value)
#
# for key, value in scores.items():
#     print(key, value)

# print(scores.setdefault('语文', 60))
# print(scores.setdefault('生物', 60), scores)

# scores = dict.fromkeys(['语文', '数学', '英语'])
# print(scores)
#
# scores = dict.fromkeys(['语文', '数学', '英语'], 90)
# print(scores)

# 根据元组格式化字符串
s1 = '图书名：%s, 价格为：%10.2f'
print(s1 % ('疯狂Python讲义', 128))

# 根据字典格式化字符串
s2 = '图书名：%(name)s, 价格为：%(price)10.2f'
print(s2 % {'price': 128, 'name': '疯狂Python讲义'})
