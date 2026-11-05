# 导入模块
import day22
print(day22.PI)
print(day22.NAME)
day22.log_separator1()
day22.log_separator2()
day22.log_separator3()
day22.log_separator4()


#导入自定义模块中的功能
# from day22 import log_separator1,log_separator3,PI,NAME
from day22 import *

#使用模块中功能
print(PI)
print(NAME)
log_separator1()
log_separator3()