"""
函数代码块以 def 关键词开头，后界函数名称和圆括号（）。
冒号起始
注意缩进
圆括号中定义参数
函数说明——文档字符串
return [表达式] 结束函数
选择性地返回一个值给调用方
不带表达式的return或者不写return函数，相当于返回None
"""


# 函数的定义
def func1(a, b, c):
    """
    函数func1的作用
    :param a: 参数a是用来打印的
    :param b:
    :param c:
    :return:
    """
    print("这是一个函数")
    print("这是一个参数a:", a)
    print("这是一个参数b:", b)
    print("这是一个参数c:", c)
    return a


# 函数的调用
result = func1("12", "df", "12")
print("函数的返回结果:", result)
