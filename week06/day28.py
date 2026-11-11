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

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []
    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        #判断学生信息是否已经存在
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败")
                return
        chinese = input("请输入学生语文成绩：")
        math = input("请输入学生数学成绩：")
        english = input("请输入学生英语成绩：")    
        #判断分数是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功~")
        else:
            print("各科成绩必须在0-100之间！")

    #修改学生成绩
    def update_student(self):
        name = input("请输入需要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")

                chinese = input("请输入修改学生语文成绩：")
                math = input("请输入修改学生数学成绩：")
                english = input("请输入修改学生英语成绩：")
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("各科成绩必须在0-100之间！")
                    return
    print("未找到该学生，修改失败！")

    #删除学生成绩
    def delete_student(self):
            name = input("请输入需要删除的学生姓名：")
            for s in self.student_list:
                if s.name == name:
                    self.student_list.remove(s)
                    print("学生信息删除成功~")
                    return
            print("未找到该学生，删除失败！")


    #查询指定学生成绩
    def query_student(self):
                name = input("请输入需要查询的学生姓名：")
                for s in self.student_list:
                    if s.name == name:
                         print(f"学生信息：{s}")
                print("未找到该学生！")
    #展示全部学生成绩
    def list_student(self):
         for s in self.student_list:
              print(s)                     
                         
