# 元组
t1 = (1, 'hello', True)
print(t1)

# 元组的操作
t2 = ('c', 'python', 'java', 'vue')
index = t2.index('c')
print(index)

# 元组的遍历
index = 0
while index < len(t2):
    print(t2[index])
    index += 1

for i in t2:
    print(i)