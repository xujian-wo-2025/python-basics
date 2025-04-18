# 定义字典
my_dict = {1: 'java', 2: 'c', 3: 'python'}
print(my_dict)


# 定义重复的key字典
my_dict = {1: 'java', 2: 'c', 3: 'python', 1: 'c++'}
print(my_dict)


# 从字典中基于key获取value
print(my_dict[2])


# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 66,
        "数学": 122,
        "英语": 70
    }, "周杰伦": {
        "语文": 77,
        "数学": 132,
        "英语": 80
    }, '林俊杰': {
        "语文": 88,
        "数学": 142,
        "英语": 90
    }
}
print(stu_score_dict)


# 从嵌套字典中获取数据
print(stu_score_dict["王力宏"]["语文"])


# 常用操作
my_dict = {"周杰伦": 90, "林俊杰": 88, "王力宏": 77}
my_dict["张学友"] = 66
print(my_dict)

my_dict.pop("周杰伦")
print(my_dict)

# 清空元素
my_dict.clear()
print(my_dict)


# 获取全部的key
my_dict = {"周杰伦": 90, "林俊杰": 88, "王力宏": 77}
print(my_dict.keys())

# 遍历
for key in my_dict.keys():
    print(my_dict[key])

for key in my_dict:
    print(my_dict[key])

# 统计字典的元素数量
print(len(my_dict))