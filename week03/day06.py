num = 1
while True:
    un = input("请输入您的账号名：")
    password = input("请输入您的密码：")
    if un == "" or password == "":
        print("输入的账号名和密码不能为空，请重新输入")
        continue
    if un == "jb" and password == "111111":
        print("登陆成功，欢迎进入b站")
        break
    elif un == "lk" and password == "000000":
        print("登陆成功，欢迎进入b站")
        break
    elif un == "kl" and password == "333333":
        print("登陆成功，欢迎进入b站")
        break
    elif num == 5:
        print("您的账号密码已输入错误5次，已被禁止操作")
        break    
    else:
        print(f"账号或密码输入错误，请重新输入，您还有",(5-num),"次机会")
        num += 1     
        continue

import random
random_num = random.randint(1,100)

while True:
    num = int(input("请输入你猜的数字："))
    if num > random_num:
        print("猜的数大了捏！")
    elif num < random_num:
        print("猜的数小了捏！")
    else:
        print("猜对了捏")
        break        

#数据容器
s = [56,48,64,1,8,4,68,48,"fxxk","hello",True]
print(type(s))
print(s[0])
print(s[-3])
s[-3] = "fuck"
print(s)
del s[-3]
print(s)
for i in s:
    print(i)
