my_set = { 'c', 'java', 'python', 'vue' ,'java'}
print(my_set)


# 添加元素
my_set.add('c++')
print(my_set)

# 移除元素
my_set.remove('c++')
print(my_set)


# 随机取出一个元素
print(my_set.pop())



# 清空集合
my_set.clear()
print(my_set)


# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(set1.difference(set2))    # {2, 3}

# 两个集合合拼为一个
print(set1.union(set2))



# 统计集合元素的个数
print(len(set2))


# 遍历只可以用for
for i in set1:
    print(i)