#导入模块
import uitls.my_fun
uitls.my_fun.log_separator1()
uitls.my_fun.log_separator2()

from uitls import my_fun

my_fun.log_separator1()
my_fun.log_separator2()
my_fun.log_separator3()

#如果通过from uitls import * 导入包下所有模块，需要__init__.py文件中添加__all__=[]
from uitls import *
my_fun.log_separator1()
my_fun.log_separator4()

print(day23.PI)
print(day23.NAME)

#导入模块中的功能

from uitls.my_fun import log_separator1,log_separator3

log_separator1()
log_separator3()