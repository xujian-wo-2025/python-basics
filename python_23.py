# 使用wile遍历列表
def list_while_func():
    my_list = ['c', 'java', 'python', 'vue']
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1

list_while_func()


# 使用for
def list_for_func():
    my_list = ['c', 'java', 'python', 'vue']
    for i in my_list:
        print(i)
list_for_func()