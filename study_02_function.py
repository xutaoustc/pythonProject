def sum(x, y):
    """
    两数相加
    :param x: 参数1
    :param y: 参数2
    :return: 返回值
    """
    return x + y


# 多返回函数
def multi_return():
    return 1, 2
x, y = multi_return()


# 全局变量
num = 10
def modify_global():
    global num   # 修改全局变量需要global，否则是定义了局部变量
    num = 20


# 关键字参数，缺省参数，不定长参数
sum(y=1, x=2)

# 默认参数必须放在最后
def default_param(a, b, c="a"):
    print(a, b, c)

def user_info(*args):
    print(type(args))

user_info(1,2,3)

