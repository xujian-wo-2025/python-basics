# 嵌套判断语句
if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果vip级别大于3，可以免费")

    if int(input("你的vip级别是多少")):
        print("恭喜你，vip级别达标，可以免费")
    else:
        print("Sorry 你需要买票")
else:
    print("欢迎小朋友, 免费游玩")