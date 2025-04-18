# 接受多个返回值
def test_return():
    return 1, 2, 3
x, y, z = test_return()
print(x,y,z)


# 位置参数
def user_info(name, age, gender='nan'):
    print(name, age, gender)

user_info("xj", 23, '男')



# 关键字参数
user_info('xj', gender='nan', age=12)


# 缺省参数
user_info('js', 12)

# 不定长
def user_info(*args):
    print(args)


user_info(1,2,3,4)


# 不定长 **
def user_info(**kwargs):
    print(kwargs)

user_info(name= 'xj', age= 12)


# 函数作为参数传递
def test_func(computer):
    result = computer(1, 2)
    print(result)

def computer(x, y):
    return  x + y


test_func(computer)