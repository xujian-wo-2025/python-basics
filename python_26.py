# 对list进行切片，冲1开始，4结束，步长为一
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[1:4])



# 对tuple进行切片，冲头开始，到最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[:])

# 对str进行切片，冲头开始，到最后结束, 步长2
my_str = '01234567'
print(my_str[::2])


# 对str进行切片，从头开始，到最后结束, 步长-1
my_str = "01234567"
print(my_str[::-1])    # 76543210