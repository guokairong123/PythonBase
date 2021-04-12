# 创建一个人类
# 通过 class 关键字，定义了一个类


class Person:
    # 类变量
    name = "default"
    age = 0
    gender = 'man'
    weight = 0

    def __init__(self, name, age, gender, weight):
        # self. 变量名的方式，访问的变量，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_weight(self, weight):
        self.weight = weight

    @classmethod
    def eat(self):
        print(f"{self.name} eating")

    def play(self):
        print(f"{self.name} playing")

    def jump(self):
        print(f"{self.name} jumping")


# 类的实例化，创建类一个实例
zs = Person('zhangsan', '20', 'man', '120')
zs.eat()
print(f"张三的名字是：{zs.name}, 张三的年龄是：{zs.age}，张三的性别是：{zs.gender}，张三的体重是：{zs.weight}")

# 类变量和实例变量的区别
# 类变量是需要类来访问的，实例变量是需要实例来访问
print(Person.name)
Person.name = 'Tom'
print(Person.name)
print(zs.name)
zs.name = 'Jam'
print(zs.name)
# 类方法和实例方法的区别
# 类方法是不能访问实例方法
# 类方法需要添加一个装饰器：@classmethod
Person.eat()
zs.eat()