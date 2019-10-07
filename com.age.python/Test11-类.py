class User:
    print('User类')


class Item:
    print('Item类')
    # 类空间中定义的变量属于类变量
    itemtype = '电子产品'
    itemcolor = '白色'


print(Item.itemtype)
print(Item.itemcolor)
# Python是动态语言，可以随时为类增加变量
Item.foo = 'Item增加一个变量foo'
print(Item.foo)
# 也可以随时删除类变量
del Item.itemtype


class Book:
    print('Book类')
    booktype = 'IT图书'

    # 定义方法与定义函数几乎一样
    # 实例方法，第一参数推荐使用self(并不强制)，这样有更好的可读性
    def dese(self):
        self.price = 118
        self.name = '疯狂Java讲义'
        print('图书是%s,价格是%d' % (self.name, self.price))

    def haha(self):
        print('我只是一个haha方法')


