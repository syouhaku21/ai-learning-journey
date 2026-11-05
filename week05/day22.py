#导入模块
import random as rd
for i in range(100):
    print(rd.randint(a=1,b=100))
#导入模块中的功能

from random import randint as rint
for i in range(100):
    print(rint(a=1,b=100))

#通配符调用
from random import *
for i in range(100):
    print(randint(a=1,b=100))


__all__ = ["log_separator1","log_separator3",PI]
#常量
PI = 3.1415926
NAME = "JB"

#函数
def log_separator1():
    print("- " * 30)#"- "重复30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

#测试代码
#__name__:python中的内置变量，表示的当前模块的名字
#执行当前文件，则会执行如下代码；如果被当成模块导入，如下代码不执行
if __name__ == '__main__':
    log_separator1()
                