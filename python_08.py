# 字符串格式化
name = "黑马程序员"
message = "学IT来：%s" %name
print(message)

class_num = 57
avg_salary = 16781
message = "python，北京%s，毕业平均工资%s" % (class_num,avg_salary)
print(message)

name = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name},我成立于{set_up_year}, 价格为{stock_price}")