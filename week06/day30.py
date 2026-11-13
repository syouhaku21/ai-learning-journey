#异常处理

try:
    print("============================")
    #print(my_name)
    print(1/0)
    print("============================")
except NameError as e:
    print("程序运行报错，错误信息：", e)
finally:
    print("释放资源~")
