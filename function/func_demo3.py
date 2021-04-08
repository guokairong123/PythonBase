"""
Lambda表达式
可以用lambda关键字来创建一个小的匿名函数。
lambda的主体是一个表达式，而不是一个代码酷块。
仅仅能在lambda表达式中封装有限的逻辑进去。
"""

func3 = lambda x: x*2

print(func3(3))


def func4(x):
    return x*2


print(func4(3))
