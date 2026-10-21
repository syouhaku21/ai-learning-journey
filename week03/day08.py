s_list = []
for i in range(10):
    num = int(input("请输入一个数："))
    s_list.append(num)
print("数字列表：",s_list)
s_list.sort()
print("排序",s_list)
print("最小值：",s_list[0])
print("最大值：",s_list[-1])
print("平均值：",sum(s_list)/len(s_list))

#去除列表重复元素
s_list1 = [1,2,3,4,56,789,87,841,6]
s_list2 = [1,513,51,5813,51543,51,5,4,3,515]
for num in s_list2:
    s_list1.append(num)
print("合并后的列表：",s_list1)
new_list = []
for num in s_list1:
    if num not in new_list:
        new_list.append(num)


print("去除重复元素后的合并列表：",new_list)    
通过解包的简化版
s_list1 = [1,2,3,4,56,789,87,841,6]
s_list2 = [1,513,51,5813,51543,51,5,4,3,515]
s_list = [*s_list1,*s_list2]

print("合并后的列表：",s_list)
new_list = []
for num in s_list:
    if num not in new_list:
        new_list.append(num)


print("去除重复元素后的合并列表：",new_list)
s_list1 = [1,2,3,4,56,789,87,841,6]
s_list2 = [1,513,51,5813,51543,51,5,4,3,515]
s_list = s_list1 + s_list2
print("合并后的列表：",s_list)
new_list = []
for num in s_list:
    if num not in new_list:
        new_list.append(num)


print("去除重复元素后的合并列表：",new_list)

s_list = []
for num in range(1,21):
    s_list.append(num**2)
print(s_list)
#简化版(列表推导式)
num_list = [i**2 for i in range(1,21)]
print(num_list)

num_new_list = []
num_list = [456,46,54,54,65,456,465,489,41,5,156,132,48,946,51]
for num in num_list:
    if num % 2 == 0:
        num_new_list.append(num**2)
print(num_new_list)
#简化版(列表推导式)
num_new_list = []
num_list = [456,46,54,54,65,456,465,489,41,5,156,132,48,946,51]
num_new_list = [num**2 for num in num_list if num % 2 == 0]
print(num_new_list) 

#数据容器：字符串
s = "hello-python"
print(s[4])
print(s[-8])
for i in s:
    print(i)

print(s[:5])
print(s[6::1])
print(s[-1:-7:-1])
                