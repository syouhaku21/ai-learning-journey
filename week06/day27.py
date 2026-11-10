class Car:
    #类属性
    wheel = 4
    tax_rate = 0.1
        
    def __init__(self,c_color,c_brand,c_name,c_price):
        #实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
    def running(self):
        print(f"{self.brand}{self.name},正在高速行驶...")
    def total_cost(self,discount,rate = 0.1):
        return self.price * discount + self.price * rate
    

c3 = Car(c_color="白色",c_brand="BYD",c_name="汉",c_price="180000")
        

print(c3.wheel)
print(c3.tax_rate)
print(Car.wheel)
print(Car.tax_rate)


class Student:
    def __init__(self,name,chinese,math,english):
        #实例属性
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{self.chinese + self.math + self.english}"
    #修改学生成绩
    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
#测试
if __name__ =='__main__':
    s1 = Student(name="王林",chinese=90,math=88,english=92)
    print(s1)

    s1.update_score(english=95)
    print(s1)

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
                print(f"学生姓名：{students_name},语文成绩：{students_info["chinese"]},数学成绩：{students_info["math"]},英语成绩：{students_info["english"]}")
                  
        case "5":#遍历所有学生信息
            if not students_infomation:
                print("暂无学生信息")
                continue
            print("姓名 \t 语文 \t 数学 \t 英语")
            for name,info in students_infomation.items():
                print(f"{students_name} \t {info['chinese']} \t {info['math']} \t {info['english']}")

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
                tops = [n for n,i in students_infomation.items() if i[key] == top]
                bottoms = [n for n,i in students_infomation.items() if i[key] == bottom]
                print(f"{sjt}最高分学生：{'、'.join(tops)}:最低分学生;{'、'.join(bottoms)}")
        case "7":#退出教务系统
            print("已退出教务管理系统")
            break

        case _:
            print("输入错误，请重新输入")