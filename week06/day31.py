#异常处理

try:
    print("============================")
    #print(my_name)
    #print(1/0)
    #print("ABC"[10])
    print("ABC".hello)
    print("============================")
except NameError as e:
    print("程序运行报错，错误信息：", e)
except ZeroDivisionError as e:
    print("0不能做被除数，异常信息：", e)
except IndexError as e:
    print("索引错误，异常信息：", e)


except Exception as e:#可以省略但不推荐
    print("程序运行出错了，请联系管理员，错误信息：", e)
finally:
    print("资源释放~")    