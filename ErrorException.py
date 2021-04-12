"""
常见的异常类型：
    除零异常、名称异常、索引异常、键异常、值异常、属性异常等等
"""


def div(a, b):
    return a/b


try:
    print(div(1, 1))
    list1 = [1, 2, 3]
    print(list1[2])
except Exception as e:
    print(e)
    print("这里有个异常")
else:
    print("没有异常时执行")
# except IndexError as e1:
#     print(e1)
finally:  # finally 最终都会被执行，无论是否有异常
    print("end")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误：{num}")
    else:
        print(f"设置的年龄为：{num}")


class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


set_age(-10)
