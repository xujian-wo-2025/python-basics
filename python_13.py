# while的嵌套循环使用
i = 1
while i <= 10:
    print(f"今天是第{i}天，准备表白。。。。")
    j = 1
    while j<=10:
        print(f"送给小美的第{j}朵玫瑰")
        j = j + 1
    print("小美我喜欢你")
    i += 1

print(f"坚持到第{i-1}天，表白成功")