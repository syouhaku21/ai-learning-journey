class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
    def running(self):
        print(f"{self.brand}{self.name},正在高速行驶...")
    def total_cost(self,discount,rate):
        return self.price * discount + self.price * rate
        

c1 = Car("red","BMW","X5",500000)
total_cost = c1.total_cost(0.9,0.1)
print(f"提车总价为:{total_price:.0f}")
c1.running()


print(c1.__dict__)        
c2 = Car("wirth","BMW","X7",700000)
print(c2.__dict__)