#函数嵌套调用
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")

function_a()
print("函数调用完毕")

def Triangle_area(b,h):
    """
    根据三角形的底长和边长求该三角形的面积
    :param b:底长
    :param h:高
    :return: 三角形面积
    """
    return  b * h / 2

print("底长为：30,高度为：20 的三角形面积：",Triangle_area(b=30,h=20))

def count_aeiou(s):#helloworld
    """
    统计字符串中的元音字母个数
    :param s:字符串
    :return 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num
print(count_aeiou("Hello Python Hello World OK"))

def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中的最高分，最低分，平均分
    :parma score_list 分数列表
    :return 最高分,最低分,平均分
    """
    max_s = max(score_list)
    min_S = min(score_list)
    avg_s = round(sum(score_list) / len(score_list),1)
    return max_s,min_S,avg_s

a_list = [578,589,579,597,587,456,789,654,987]
max_score,min_score,avg_score = calc_score(a_list)
print("最高分：",max_score)
print("最低分：",min_score)
print("平均分：",avg_score)




   