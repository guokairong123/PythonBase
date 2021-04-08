# 猜数字游戏
import random

computer_num = random.randint(1, 100)
while True:
    person_num = int(input("请输入一个数字:"))
    # print(computer_num)
    if computer_num > person_num:
        print("大一些")
    elif computer_num < person_num:
        print("小一些")
    elif computer_num == person_num:
        print("猜对了")
        flag = input("是否继续？ 输入Y/N:")
        if flag == "Y" or flag == "y":
            computer_num = random.randint(1, 100)
            continue
        elif flag == "N" or flag == "n":
            break
        else:
            print("非法输入值，已退出游戏")
            break
