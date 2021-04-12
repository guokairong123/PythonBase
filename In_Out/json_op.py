"""
json.dumps(python_obj)  把数据类型转换为字符串
json.loads(json_string) 把字符串转换成json
json_dump()             把数据类型转换成字符串并存储在文件中
json.load(file_stream)  把文件打开，把里面的字符转换成数据类型
"""
import json

data = {
    "name": ["Mike", "Tom"],
    "age": 26,
    "gender": "man"
}
data1 = json.dumps(data)
print(data1)
print(type(data1))
data2 = json.loads(data1)
print(type(data2))