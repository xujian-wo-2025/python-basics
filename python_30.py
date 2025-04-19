# 异常
try:
    f = open('D:/ABC.txt','r',encoding='utf-8')
except:
    print('文件报错了')




# 捕获指定的异常
try:
    1/0
except NameError as e:
    print("出现了未定义异常")



# 捕获多个异常
try:
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print("变量未定义或者除数为0")


try:
    f = open('D:/ABC.txt','r',encoding='utf-8')
except:
    print("出现异常了")
else:
    print("好高兴，没有异常")
finally:
    f.close()