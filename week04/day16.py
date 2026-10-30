#全局变量
num = 100

#定义函数
def circle_area(r):#一个用法
    #局部变量
    pi = 3.14
    area = pi * r * r

    global num #变为全局变量
    num = 10000
    print("num =",num)
    return area

c_area = circle_area(10)
print(c_area)

print("num =",num)

def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
#位置传参
stu = reg_stu("张三",18,"男","北京")
print(stu)
#关键字传参
stu2 = reg_stu(name="赵四",city="桂林",age=29,gender="男")
print(stu2)

#默认参数
def reg_stu(name,age,gender,city='桂林'):
    print(f"注册成功,姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
stu = reg_stu("王林",19,"男")
print(stu)
stu2 = reg_stu("李慕婉",19,"女","京城")
print(stu2)
