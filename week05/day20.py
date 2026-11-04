#电商订单计算器
'''
定义一个函数，用于根据传入的一批商品信息(商品名，价格，数量),优惠(优惠券，积分抵扣),运费信息计算订单的总金额函数
'''
def calc_order_cost(*args,coupon=0,score=0,express=0):
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

total = calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.9)            
print(total)

#数据类型
a2: int = 596
score2: float = 98.8
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str|int] = ["A","B","C"]
phone2: set[str] = {"13377310706","13377300706","13377000706"}
options2: dict[str,int] = {"count":2,"total":10}
goods2: tuple[str,int,int] = ("手机",6999,1)

names2.append(100)
names2.append("S")

