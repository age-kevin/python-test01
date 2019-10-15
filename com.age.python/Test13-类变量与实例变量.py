# class User:
#     # 类空间中定义的变量，是类变量
#     category = '未知类型'
#
#     def __init__(self, name='admin', passwd='passwd'):
#         self.name = name
#         self.passwd = passwd
#
#
# # 通过类引用赋值的变量,也属于类变量
# User.type = '通用用户'
#
# print(User.category)
# User.category = '整型'
# print(User.category)
#
# u = User()
# # 当对象本身没有category实例变量时，对象可访问该类变量
# print(u.category)
# # 只要通过对象对变量赋值，就变成了新增实例变量
# u.category = '实例类型'
# # 当对象本身已有category实例变量时，对象优先访问实例变量
# print(u.category)
# # 此处依然是访问类变量
# print(User.category)

# 实例变量不在类空间下，类不能访问实例变量，只能通过对象来访问实例变量


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

    # 合成一个计算面积的属性
    area = property(fget=getarea, doc='获取面积的属性')

    def getsize(self):
        return self.width, self.height

    def setsize(self, size):
        self.width = size[0]
        self.height = size[1]

    # 合成一个代表大小的属性
    size = property(fget=getsize, fset=setsize, doc='代表大小的属性')


r = Rectangle(30, 40)
# 访问area变量实际上就是调用getter方法
print(r.area)
