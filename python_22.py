# 列表及常用方法
list_name = ['python', 'c', 'java', 'php', 'vue']
# index 查找指定元素在列表的下标
index = list_name.index('java')
print(index)


# 修改元素
list_name[0] = 'Python'
print(list_name)

# 插入
list_name.insert(1, 'js')
print(list_name)


# 追加元素
list_name.append('element')
print(list_name)


# 删除元素
list_name.pop(6)
print(list_name)


# 清空列表
list_name.clear()
print(list_name)


# 统计元素的个数
list_name = [1,2,3,1,12,3,1,3]
print(list_name.count(1))