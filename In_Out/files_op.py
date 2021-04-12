#
# f = open('data.txt')
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# f.close()
"""
with 语句块，可以将文件打开，操作完毕后，自动关闭这个文件
图片读取需要使用rb，读取二进制格式
正常的文本，可以使用rt，也就是它的默认格式即可
"""
with open('data.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.readlines())
