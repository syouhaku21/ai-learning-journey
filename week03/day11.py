#set集合(无序，不可重复，可修改)
s1 = {"A","B","C","D","E","F","C"}
print(s1)
print(type(s1))

s2 = {}
print(type(s2))

s1 = set() #空集合

one_set = {"A","B","C","D","E","F","G","H","I","Z"}
two_set = {"B","C","D","E","R","T","J","Y","G","N","K","Q","W","O","P"}
three_set = {"V","E","R","B","C","G","W","J","K"}
four_set = {"A","V","B","N","M","E"}

#同时选择了3和4的字母
# tf_set = three_set.intersection(four_set)
tf_set = three_set & four_set
print(tf_set)
#同时选择了1到4的字母
ottf_set = one_set & two_set & three_set & four_set
print(ottf_set)

#找到选了1但是没选2的字母
# to_set = one_set.difference(two_set)
to_set = one_set - two_set
print(to_set)
#快速构建集合：{要往集合增加的数据 for s in setl if 条件}
to_set2 = {s for s in one_set if s not in two_set}
print(to_set2)

#统计每一个字母的选择量
# all_set = one_set.union(two_set).union(three_set).union(four_set)
all_set = one_set | two_set | three_set | four_set
print(all_set)
#把集合内元素全都解包进列表即可重复
all_list = [*one_set,*two_set,*three_set,*four_set]
for s in all_set:
    print(f"{s} 选择了 {all_list.count(s)} 次")



