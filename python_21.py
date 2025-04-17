# 函数的嵌套调用
def func_b():
    print("22222222222222")
def func_a():
    print("11111111111111")
    func_b()
    print("33333333333333")
func_a()