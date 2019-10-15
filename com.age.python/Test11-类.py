# from types import MethodType
# class User:
#     print('User类')
#
#
# class Item:
#     print('Item类')
#     # 类空间中定义的变量属于类变量
#     itemtype = '电子产品'
#     itemcolor = '白色'
#
#
# print(Item.itemtype)
# print(Item.itemcolor)
# # Python是动态语言，可以随时为类增加变量
# Item.foo = 'Item增加一个变量foo'
# print(Item.foo)
# # 也可以随时删除类变量
# del Item.itemtype
#
#
# class Book:
#     print('Book类')
#     booktype = 'IT图书'
#
#     # 定义方法与定义函数几乎一样
#     # 实例方法，第一参数推荐使用self(并不强制)，这样有更好的可读性
#     def dese(self):
#         self.price = 118
#         self.name = '疯狂Java讲义'
#         print('图书是%s,价格是%d' % (self.name, self.price))
#
#     def haha(self):
#         print('我只是一个haha方法')
#
#


# class Person:
#     # 构造方法
#     def __init__(self, name='kevin', age=8):
#         print('构造方法')
#         self.name = name
#         self.age = age
#
#
# # 创建对象，就是调用构造器
# # 调用构造方法，不是直接调用__init__方法，而是通过类名来调用
# p = Person()
# print(p.name, p.age)
# p2 = Person('孙悟空')
# print(p2.name, p2.age)
# p3 = Person(age=30)
# print(p3.name, p3.age)
# p4 = Person('白骨精', 100)
# print(p4.name, p4.age)
#
#
# class Teacher:
#     pass


# class Item:
#     def __init__(self, name='鼠标'):
#         self.name = name
#
#
# # 访问实例变量：显示器
# im1 = Item('显示器')
# print(im1.name)
#
# # 访问实例变量：鼠标
# im2 = Item()
# print(im2.name)
#
# # 新增实例变量:对不存在的变量赋值
# im2.color = '黑色'
# print(im2.color, im2.name)
#
# # 删除实例变量
# del im2.name
# print(im2.name)


# class Item:
#     # 实例方法属于对象，用对象调用
#     def test(self):
#         print('test')
#
#
# im1 = Item()
# # 调用方法
# im1.test()
#
#
# def fn(self):
#     print('新增的方法')
#
#
# # 增加方法
# im1.foo = fn
# # 新增的方法，默认不会自动绑定self参数，self参数必须手动传入参数值
# im1.foo(im1)
#
# # 将fn函数包装成方法，且im1自动绑定第一个参数
# im1.bar = MethodType(fn, im1)
# im1.bar()
#
# # 删除方法
# del im1.test


# class User:
#     def __init__(self, name='kevin'):
#         # self代表该构造器正在构造的对象
#         self.name = name
#
#     def info(self):
#         print(self)
#         print(self.name)
#
#
# # User构造的对象，就赋值给了u，在User构造器中的self实际上就代表了u
# u1 = User()
# print(u1.name)
#
# # User构造的对象，就赋值给了u2，在User构造器中的self实际上就代表了u2
# u2 = User('scott')
# print(u2.name)
#
# print(u2)
#
# # -----实例方法第一个self参数不需要传入，由系统自动绑定，总是绑定到方法调用者-----
# # -----方法中的self总是代表该方法的调用者-----
#
# # 程序用u2调用info方法，那么info方法中的self就代表了u2
# u2.info()
# # 程序用u1调用info方法，那么info方法中的self就代表了u1
# u1.info()


# class Dog:
#     def run(self):
#         # 一个方法调用其他方法，也需要使用self来调用
#         self.jump()
#         print('狗在跑')
#
#     def jump(self):
#         print('狗在跳')
#
#
# d = Dog()
# d.run()


# class Plant:
#     def __init__(self, height=2):
#         self.height = height
#
#     def grow(self):
#         # 每grow一次，height增加10
#         self.height += 10
#         return self
#
#
# p = Plant()
# print(p.height)
# # 如果你的grow方法return了self，而self本身又代表方法调用者p
# p.grow().grow().grow().grow()
# print(p.height)


# class Role:
#     def test(self):
#         print('test方法')
# 
# 
# # test方法本身是实例方法，应该用对象调用，但Python允许用类调用实例方法，此时变成了‘未绑定方法’，因此必须显式地为self参数传入参数值
# r = Role()
# Role.test(r)


# class Tiger:
#     # 类方法：A、用@classmethod修饰；B、定义一个cls形参
#     @classmethod
#     def info(cls):
#         print('info类方法')
#         print(cls)
#
#
# print(Tiger)
# # 类方法属于类本身，因此用类来调用
# # 类方法的第一个参数也会自动绑定，绑定到调用该方法的类
# Tiger.info()
#
# t = Tiger()
# # 对象调用类方法，实际上也相当于用类调用类方法，同样也会执行自动绑定
# t.info()


class Tiger:
    # 静态方法：A、用@staticmethod修饰。B、无需定义任何形参
    @staticmethod
    def info(p):
        print('info静态方法')
        print(p)


# 静态方法相当于一个函数，因此不会自动绑定
# 类调用静态方法
Tiger.info('Kevin')

# 对象调用静态方法，也不会自动绑定，因此必须为参数传入参数值
t = Tiger()
t.info('Age')

