
#定义类--->不推荐
class Car:
    pass
#创建对象
c1 = Car()
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1.__dict__)#对象中的属性以字典形式输出

class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
c1 = Car("red","BMW","X5",500000)
print(c1.__dict__)        
c2 = Car("wirth","BMW","X7",700000)
print(c2.__dict__)    