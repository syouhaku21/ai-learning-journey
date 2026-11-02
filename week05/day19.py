def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

#计算
def calc(x,y,oper):
    return oper(x,y)

print(calc(x=10,y=20,oper=multiply))
# 匿名函数
out_line = lambda :print("----------------")
out_line()

add = lambda x , y:x + y
print(add(x=100,y=200))
#匿名函数运用场景
data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
data_list.sort(key=lambda item :len(item),reverse=True)
print(data_list)

#定义一个函数，根据传入的数字，计算该数字阶乘的结果。
def jc(n):
    if n == 1:#递归调用,一定要有终结点
        return 1
    else:
        return n * jc(n - 1) 
result = jc(10)
print(result)
    


