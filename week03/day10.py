# t1 = (8,1,5,651,6521,564,561,651,651,56)
# print(t1)
# print(type(t1))

# print(t1[0])
# print(t1[-1])

# print(t1[0:5:1])
# #count(统计元素个数)
# print(t1.count(8))
# #index(获取检索元素位置)
# print(t1.index(1))

# t2 = (5,)
# print(t2)
# print(type(t2))
# #元组的组包解包
# t1 = (2,3,5,7,9,10)
# t2 = 5,7,9,10

# a,b,c,d,e,f = t1
# x,*y,z = t2
# s,*o = t2
# *o,e = t2

# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)

# *other,last2,last1 = t1
# print(other)
# print(last2)
# print(last1)

# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

# x = 100
# y = 200
# z = 300

# z,x,y = x,y,z
# print(x)
# print(y)
# print(z)

students = (
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","近天",66,59,72)
)
#1计算总分平均分然后输出
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    print(f"{i[0]}\t {i[1]}\t {i[2]}\t {i[3]}\t {i[4]}\t {total}\t {avg:.1f}")
print()
#统计各科最低分最高分平均分
ch_sc = [s[2] for s in students]
print(ch_sc)
mt_sc = [s[3] for s in students]
print(mt_sc)
el_sc = [s[4] for s in students]
print(el_sc)

print(f"语文最低分为：{min(ch_sc)},最高分为：{max(ch_sc)},平均分为：{sum(ch_sc)/len(ch_sc)}")
print(f"数学最低分为：{min(mt_sc)},最高分为：{max(mt_sc)},平均分为：{sum(ch_sc)/len(mt_sc)}")
print(f"英语最低分为：{min(el_sc)},最高分为：{max(el_sc)},平均分为：{sum(el_sc)/len(el_sc)}")
print()
#查询出优秀学生成绩并输出
print("优秀学生(平均分大于90)名单如下:")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    if avg > 90:
        print(f"学号：{i[0]}姓名：{i[1]} 平均分：{avg:.1f}成绩优秀！继续精进！")    
