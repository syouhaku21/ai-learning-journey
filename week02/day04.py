score = int(input("请输入您的考试分数："))
if score >= 85:
    print(f"您的成绩为{score},相当优秀。")
elif score < 85 and score >= 60:
    print(f"您的成绩为{score},还需加油。")
else:
    print(f"您的成绩为{score},不合格！")
a_sl = int(input("请输入三角形的第一边长："))
b_sl = int(input("请输入三角形的第二边长："))
c_sl = int(input("请输入三角形的第三边长："))
if a_sl == b_sl == c_sl:
    print("这个三角形三边相等，是等边三角形")
elif (a_sl == b_sl or a_sl == c_sl or b_sl == c_sl) and a_sl + b_sl >c_sl and a_sl + c_sl > b_sl and b_sl + c_sl > a_sl:
    print("这个三角形两边相等，是等腰三角形")
elif a_sl + b_sl > c_sl and a_sl + c_sl > b_sl and b_sl + c_sl > a_sl:
    print("这个三角形三边不等，是普通三角形")
else:
    print("这边长不符合要求，不是三角形")
day = input("请输入星期几（1-7）：")
match day:
    case "1":
        print("周一")   
    case "2":
        print("周二")
    case "3":
        print("周三")
    case "4":
        print("周四")
    case "5":
        print("周五")
    case "6" | "7":
        print("周末")
    case _:
        print("输入有误！")     
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
pjt = input("请输入计算方法（+,-,*,/）：")
match pjt:
    case "+":
        print(f"结果为：{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"结果为：{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"结果为：{num1} * {num2} = {num1 * num2}") 
    case "/" if num2 != 0:
        print(f"结果为：{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作错误！")              
in_p = input("请输入指令：")
match in_p:
    case "w"|"W":
        print("角色向上移动")
    case "a"|"A":
        print("角色向左移动")
    case "s"|"S":
        print("角色向下移动")
    case "d"|"D":
        print("角色向下移动")
    case " ":
        print("角色跳跃")
    case "j"|"J":
        print("角色普通攻击")
    case "esc"|"ESC":
        print("玩家推出游戏")
    case _:
        print("指令输入错误")    
i = 0
while i < 10:
    print("人生苦短，我用python~")
    i += 1
else:
    print("循环正常结束，执行完毕。")
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100之间的偶数的累计之和：{total}")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j:<2}",end='\t')
        j += 1
    print()
    i += 1 
else:
    print("99乘法表输出完成")
        
msg = input("请输入需要遍历的字符串：")

for s in msg:
    print(f"元素：{s}")

else:
    print("遍历结束！")

total = 0
for s in range(1,101):
    if s % 2 == 1:
        total += s
    
print("1-100之间基数累加之和：",total)
total = 0
for s in range(1,101,2):
    total += s
print("1-100之间基数之和为：",total)    

total = 0
for s in range(100,501):
    if s % 3 == 0:
        total += s   
print("100-500之间3的倍数累加之和：",total)

m = int(input("请输入长方形长度："))
n = int(input("请输入长方形宽度："))
for s in range(m):
    for i in range(n):
        print("*",end="\t")
    print()