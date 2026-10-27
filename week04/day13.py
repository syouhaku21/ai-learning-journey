# shopping_cart = {}
# #1制作菜单
# menu = """
# ########## 购物车系统 #########
# #         1.添加购物车        #         
# #         2.修改购物车        #         
# #         3.删除购物车        #         
# #         4.查询购物车        #         
# #         5.退出购物车        #         
# ##############################
# """

# print("欢迎使用购物车管理系统~")

# while True:
#     print(menu)
#     #2执行的操作
#     choice = input("请选择执行的操作(1-5):")
#     match choice:
#         case "1":#添加购物车
#             goods_name = input("请输入商品名称：")
#             goods_price = input("请输入商品价格：")
#             goods_num = input("请输入商品数量：")

#             #如果商品存在则无法加入购物车
#             if goods_name in shopping_cart:
#                 print("商品已存在，请重新选择")
#             else:
#                 shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
#                 print("商品添加完毕~")

                    
#         case "2":#修改购物车
#             goods_name = input("请输入要修改的商品名称：")
#             #如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择！")
#                 continue
#             goods_price = input("请输入商品最新的价格：")
#             goods_num = input("请输入商品最新的数量：")

#             shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
#             print("商品已修改完毕~")

        
#         case "3":#删除购物车
#             goods_name = input("请输入要删除的商品名称：")

#             #如果商品不存在，则提示错误信息，请重新选择
#             if goods_name not in shopping_cart:
#                 print("商品不存在，请重新选择！")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品已删除完毕~")
#         case "4":#查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
#         case "5":#退出购物车
#             print("已退出购物车~")
#             break
#         case _:
#             print("非法操作，不支持")
#棋盘练习
# for i in range(8):
#     for s in range(8):
#         if (i + s) % 2 == 0:
#             print("■",end=" ")
#         else:
#             print("□",end=" ")
#     print()
# print("棋盘已生成") 

students_infomation = {}
aasas = '''
######### 教务管理系统 #########
#         1.添加学生信息       #         
#         2.修改学生信息       #         
#         3.删除学生信息       #         
#         4.查询学生信息       #         
#         5.列出学生信息       #
#         6.统计班级成绩       #
#         7.退出教务系统       #         
###############################           
'''    
print("已进入教务管理系统~")
while True:
    print(aasas)
    choice = input("请选择对应服务(1-7)：")
    match choice:
        case "1":#添加学生信息
            students_name = input("请输入学生姓名：")
            students_chinese = int(input("请输入学生语文成绩："))
            students_math = int(input("请输入学生数学成绩："))
            students_english = int(input("请输入学生英语成绩："))
            if students_name in students_infomation:
                print("学生已录入请重新输入~")        
            else:
                students_infomation[students_name] = {"chinese":students_chinese,"math":students_math,"english":students_english}
                print(f"添加【students_name】成功")
        case "2":#修改学生信息
            students_name = input("请输入要修改的学生姓名：")
            if students_name not in students_infomation:
                print("该学生不存在，请重新输入！")
                continue
            students_chinese = int(input("请输入学生语文成绩："))
            students_math = int(input("请输入学生数学成绩："))
            students_english = int(input("请输入学生英语成绩："))
            students_infomation[students_name] = {"chinese":students_chinese,"math":students_mach,"english":students_english}

        case "3":#删除学生信息
            students_name = input("请输入要删除的学生姓名：")
            if students_name not in students_infomation:
                print("该学生不存在，请重新输入！")
                continue
            else:
                del students_infomation[students_name]
                print("学生信息已删除~")

        case "4":#查询学生信息
            for students_name in students_infomation.keys():
                students_info = students_infomation[students_name]
                print(f"学生姓名：{students_name},语文成绩：{students_info["chinese"]},数学成绩：{students_info["math"]},英语成绩：{students_info["english"]}")
                  
        case "5":#遍历所有学生信息
            if not students_infomation:
                print("暂无学生信息")
                continue
            print("姓名 \t 语文 \t 数学 \t 英语")
            for name,info in students_infomation.items():
                print(f"{students_name} \t {info['students_chinese']} \t {info['students_math']} \t {info['students_english']}")

        case "6":#统计班级成绩
            if not students_infomation:
                print("暂无学生信息")
                continue
            chinese_list = [info["students_chinese"] for info in students_infomation.values()]
            math_list = [info["students_math"] for info in students_infomation.values()]
            english_list = [info["students_english"] for info in students_infomation.values()]
            print(f"语文：最高 {max(chinese_list)}，最低 {min(chinese_list)}，平均 {sum(chinese_list)/len(chinese_list):.1f}")
            print(f"数学：最高 {max(math_list)}，最低 {min(math_list)}，平均 {sum(math_list)/len(math_list):.1f}")
            print(f"英语：最高 {max(english_list)}，最低 {min(english_list)}，平均 {sum(english_list)/len(english_list):.1f}")
            for sjt,sc in[("语文",chinese_list),("数学",math_list),("英语",english_list)]:
                top = max(sc)
                bottom = min(sc)
                tops = [n for n,i in students_infomation.items() if i[sjt] == top]
                bottoms = [n for n,i in students_infomation.items() if i[sjt] == bottom]
                print(f"{sjt}最高分学生：{'、'.join(tops)}:最低分学生;{'、'.join(bottoms)})")
        case "7":#退出教务系统
            print("已退出教务管理系统")
            break

        case _:
            print("输入错误，请重新输入")    












