# 使用import导入time模块的使用sleep
import time

# 使用from导入time的sleep功能
from time import sleep
sleep(5)


# 导入自定义包中的模块
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()