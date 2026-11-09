class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
    def running(self):
        print(f"{self.brand}{self.name},正在高速行驶...")
    def total_cost(self,discount,rate = 0.1):
        return self.price * discount + self.price * rate
    def __str__(self):
        return f"{self.color}{self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name
    def __lt__(self, other):
        return self.price < other.price


c3 = Car(c_color="白色",c_brand="BYD",c_name="汉",c_price="180000")
print(c3)
c4 = Car(c_color="白色",c_brand="BYD",c_name="秦",c_price="160000")
print(c4)
c1 = Car("red","BMW","X5",500000)        

print(c3 == c4)
print(c3 > c4)
# c1.running()
# total = c1.total_cost(0.9,0.1)
# print("提车总价为:",total)
# tota2 = c1.total_cost(0.9,0.1)
# print("提车总价为:",tota2)

print()