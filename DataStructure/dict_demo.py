# 字典的定义
hogwarts_dict = {"a": 1, "b": 2}
hogwarts_dict2 = dict(a=1, b=2)

print("hogwarts_dict:", hogwarts_dict)
print(type(hogwarts_dict))
print("hogwarts_dict2:", hogwarts_dict2)
print(type(hogwarts_dict2))

# 字典的操作
a = {"a": 1, "b": 2}
b = dict(a=1, b=2)

print(a.keys())
print(a.values())
# print(a.pop("a"))
# 随机删除一个键值对
print(a.popitem())
print(a)

c = {}
d = c.fromkeys([1, 2, 3], "A")
print(d)