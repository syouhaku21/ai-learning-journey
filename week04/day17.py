#不定长位置传参数
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data,max_data,round(avg_data,1)

print(calc_data(2,7,9,10,45))
print(calc_data(2,7,9,10,45,73,37.93,92,111,222))

不定长关键字传参数

def calc_data(*args,**kwargs):
    '''
    根据传入的这批数据，计算这批数据的最小值，最大值，平均数
    :param args:不定长位置参数，需要计算的这批数据
    :param kwargs:不定长关键字参数
        round:保留小数位数
        print:是否打印输出
    :return:输出最小值，最大值，平均值
    '''
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round")  is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值：{min_data},最大值：{max_data},平均值：{avg_data}")    

    return min_data,max_data,avg_data

# print(calc_data(2,7,9,10,45,round = 3,print = True))
print(calc_data(2,7,9,10,45,73,37.93,92,111,222,round = 3,print = False))
