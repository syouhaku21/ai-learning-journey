for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end='\t')
    print()
else:
    print("输出完成")

num = int(input("请输入三角形的直角边长："))

for i in range(1,num + 2):
    for j in range(1,i):
        print("*",end='  ')
    print()       
else:
    print("输出完成")

num = int(input("请输入数字金字塔的长度："))
for i in range(1,num + 2):
    for j in range(1,i):
        print(j,end='  ')
    print()
else:
    print("输出完成")

for i in range(1,9):
    for j in range(1,9):
        if (i + j) % 2 == 0:
            print("■",end=' ')
        else:
            print("□",end=' ')
    print()        
print("棋盘已生成")

import random
num1 = random.randint(1,100)
while True:
    num = int(input("请输入您猜的数字（1~100）："))
    if num > num1:
        print("你猜的数大了捏！")
    elif num < num1:
        print("你猜的数小了捏！")
    else: 
        print("你猜对了哦")
        break
print("游戏结束")
 