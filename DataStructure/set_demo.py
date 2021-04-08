# 集合的定义
# a = {1}
# b = set()
#
# print(type(a))
# print(type(b))

# 集合的操作
a = {1, 2, 3}
b = {1, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
a.add("a")
print(a)

print({i for i in "dsffdsghjdsghsahgjfhgsdgh"})
# 去重
c = "asdsadasdasdsaddasd"
print(set(c))
