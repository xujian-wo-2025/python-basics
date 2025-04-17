# 函数初体验(统计字符串的长度
str1 = 'itheima'
str2 = 'itcast'
str3 = 'python'

count = 0
# for i in str1:
#     count+=1
# print(f"字符串的长度{count}")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度{count}")
my_len(str1)