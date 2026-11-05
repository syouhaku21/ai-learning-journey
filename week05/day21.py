def calc(scores:list[int]) -> float:
    return sum(scores) / len(scores)

#电商订单计算器
'''
定义一个函数，用于根据传入的一批商品信息(商品名，价格，数量),优惠(优惠券，积分抵扣),运费信息计算订单的总金额函数
'''
def calc_order_cost(*args:tuple[str,float,int],coupon:int=0,score:int=0,express:float=0):
    """
    根据传入的一批商品信息(商品名，价格，数量),优惠(优惠券，积分抵扣),运费信息计算订单的总金额
    :param args:商品信息(商品名，价格，数量)---> 如:("鼠标"，188,2)
    :param coupon
    :param score
    :param express
    :return: 订单总金额
    """
#订单总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
# 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)


#扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -=  coupon
#扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
#添加运费
    total_cost += express
    return total_cost

total = calc_order_cost(("鼠标",88.5,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.9)            
print(total)



import random
names = ["王琳","李慕婉","徐立国","韩立","涛哥","魔礼海","十三","虎跑"]