age = 10
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过的真快")


# if else 组合使用
print("欢迎来到南昌之星,成年人要补票，未成年免费")
age = int(input("请输入你的年龄"))
if age >= 18:
    print("你已成年，需要买票")
else:
    print("你未成年，免费游玩")
print("祝你玩的愉快")



# if elif else语句组合使用
print("欢迎来到南昌之星")
# height = int(input("请输入你的身高："))
# vip_level = int(input("请输入你的VIP等级(1-5): "))

if int(input("请输入你的身高：")) <= 120:
    print("身高小于120cm，免费")
elif int(input("请输入你的VIP等级(1-5): ")) > 3:
    print("vip级别大于3：免费")
else:
    print("不好意思，条件都不满足，需要买票10元")