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
                print(f"添加【{students_name}】成功")
        case "2":#修改学生信息
            students_name = input("请输入要修改的学生姓名：")
            if students_name not in students_infomation:
                print("该学生不存在，请重新输入！")
                continue
            students_chinese = int(input("请输入学生语文成绩："))
            students_math = int(input("请输入学生数学成绩："))
            students_english = int(input("请输入学生英语成绩："))
            students_infomation[students_name] = {"chinese":students_chinese,"math":students_math,"english":students_english}

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
                print(f"学生姓名：{students_name},语文成绩：{students_info["students_chinese"]},数学成绩：{students_info["students_math"]},英语成绩：{students_info["students_english"]}")
                  
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
            key_map = {
                "语文":"chinese",
                "数学":"math",
                "英语":"english"
            }
            chinese_list = [info["chinese"] for info in students_infomation.values()]
            math_list = [info["math"] for info in students_infomation.values()]
            english_list = [info["english"] for info in students_infomation.values()]
            print(f"语文：最高 {max(chinese_list)}，最低 {min(chinese_list)}，平均 {sum(chinese_list)/len(chinese_list):.1f}")
            print(f"数学：最高 {max(math_list)}，最低 {min(math_list)}，平均 {sum(math_list)/len(math_list):.1f}")
            print(f"英语：最高 {max(english_list)}，最低 {min(english_list)}，平均 {sum(english_list)/len(english_list):.1f}")
            for sjt,sc in[("语文",chinese_list),("数学",math_list),("英语",english_list)]:
                key = key_map[sjt]
                top = max(sc)
                bottom = min(sc)
                tops = [n for n,i in students_infomation.items() if i[sjt] == top]
                bottoms = [n for n,i in students_infomation.items() if i[sjt] == bottom]
                print(f"{sjt}最高分学生：{'、'.join(tops)}:最低分学生;{'、'.join(bottoms)}")
        case "7":#退出教务系统
            print("已退出教务管理系统")
            break

        case _:
            print("输入错误，请重新输入")