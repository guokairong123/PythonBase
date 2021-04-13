import time

# # 国外的时间格式
# print(time.asctime())
# # 时间戳
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))