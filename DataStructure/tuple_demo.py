# 元组的定义
# tuple_hogwarts = (1, 2, 3)
# tuple_hogwarts2 = 1, 2, 3
# print("tuple_hogwarts:", tuple_hogwarts)
# print("tuple_hogwarts2:", tuple_hogwarts)
# print(type(tuple_hogwarts))
# print(type(tuple_hogwarts2))

# 元组的不可变特性
# list_hogwarts = [1, 2, 3]
# list_hogwarts[0] = 'a'
# print(list_hogwarts)
#
# tuple_hogwarts = (1, 2, list_hogwarts)
# print(id(tuple_hogwarts[2]))
# tuple_hogwarts[2][1] = 'b'
# print(id(tuple_hogwarts[2]))
# print(tuple_hogwarts)

# 元组的操作
a = (1, 2, 3, "a", "b", "a")
print(a.count("a"))
print(a.index("a"))