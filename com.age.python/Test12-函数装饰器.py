# 作为函数装饰器使用的参数，必须定义一个形参
# def foo(fn):
#     print('foo函数')
#     print(fn)
#     return 'kevin'


# 被装饰的函数
# @foo
# def bar():
#     print('bar函数')


"""
    函数装饰器的本质：
        1、将被装饰的函数(bar)作为参数传给装饰器函数(foo)
        2、被装饰的函数(bar)将被替换成装饰器函数(foo)的返回值

"""
# bar被装饰——被替换成装饰器的返回值：kevin
# print(bar)


# 装饰器模式类似Java的AOP
def foo(fn):
    print('foo装饰器函数')
    print(fn)

    def noname(*args):
        print('----------目标函数之前植入代码----------')
        fn(*args)
        print('----------目标函数之后植入代码----------')

    return noname


@foo
def test(a, b):
    print('test函数')
    print('参数a：', a)
    print('参数b：', b)


test(2, 4)


