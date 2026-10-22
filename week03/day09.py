# s = ("hello-world-hello-python")
# index = s.find("-")
# print(index)

# c = s.count("o")
# print(c)

# su = s.upper()
# print(su)

# sl = s.lower()
# print(sl)

# slist = s.split("-")
# print(slist)
# #去除字符串中前后空格
# ss = s.strip()
# print(ss)

# sr = s.replace("-","+")
# print(sr)

# print(s.startswith("hello"))
# print(s.endswith("world"))

# print("------------------------------------------")
# print(s)

# em = input("请输入您的邮箱：")
# if em.count("@") == 1 and em.count(".") >= 1:
#     print("邮箱格式正确。")
# else:
#     print("邮箱格式错误。")    

# em = input("请输入您的邮箱：")
# if em.count("@") == 1 and "." in em:
#     print("邮箱格式正确。")
# else:
#     print("邮箱格式错误。")

# s = int(input("请输入一个字符串："))
# if s == s.reverse:
#     print("这是一个回文。")
# else:
#     print("这不是一个回文。")
#判断输入字符串是否为回文
# s = input("请输入一个字符串：")

# reversed_s = ""          # 空字符串，准备接收
# for ch in s:
#     reversed_s = ch + reversed_s   # 每个新字符都加到最前面

# if s == reversed_s:
#     print("这是一个回文。")
# else:
#     print("这不是一个回文。")
#将输入的字符串改为大写切记进列表，最后把列表遍历
a_list = []
for i in range(10):
    str_m = input("请您输入一个字符串：")
    str_m = str_m[::-1]
    a_list.append(str_m.upper())
    
for item in a_list:
    print(item)
    
    


    
