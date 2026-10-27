name_list = ["A","B","C","D","E","F","G"]
sc_list = [670,556,582,608,512,678,456]
dict1 = {"A":670,"B":556,"C":582,"D":608,"E":512,"F":678,"G":456}




shopping_cart = {}
#1制作菜单
menu = """
########## 购物车系统 #########
#         1.添加购物车        #         
#         2.修改购物车        #         
#         3.删除购物车        #         
#         4.查询购物车        #         
#         5.退出购物车        #         
##############################
"""

print("欢迎使用购物车管理系统~")

while True:
    print(menu)
    #2执行的操作
    choice = input("请选择执行的操作(1-5):")
    match choice:
        case "1":#添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = input("请输入商品价格：")
            goods_num = input("请输入商品数量：")

            #如果商品存在则无法加入购物车
            if goods_name in shopping_cart:
                print("商品已存在，请重新选择")
            else:
                shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
                print("商品添加完毕~")

                    
        case "2":#修改购物车
            goods_name = input("请输入要修改的商品名称：")
            goods_price = input("请输入商品最新的价格：")
            goods_num = input("请输入商品最新的数量：")

            #如果商品不存在，则提示错误信息，重新选择
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择！")
            else:
                shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
                print("商品已修改完毕~")

        
        case "3":#删除购物车
            goods_name = input("请输入要删除的商品名称：")

            #如果商品不存在，则提示错误信息，请重新选择
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择！")
            else:
                del shopping_cart[goods_name]
                print("商品已删除完毕~")
        case "4":#查询购物车
            for goods_name in shopping_cart.keys():
                shopping_cart[goods_name]
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
        case "5":#退出购物车
            print("已退出购物车~")
            break
        case _:
            print("非法操作，不支持")                