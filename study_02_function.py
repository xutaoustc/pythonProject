
def hello_world():
    print("hello world")
    # 分割打印
    print("还剩余", 1, "元")
    # 不换行的print
    print("hello", end=" ")
    print("world", end="")


def multi_return():
    """
    多返回函数
    :return:
    """
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

