# 数字 - 整数、浮点数、布尔
# 字符串
# 列表 - 有序可变序列
# 元组 - 有序不可变序列
# 集合 - 无序不重复集合
# 字典

"""
this is a comment
"""

def helloWorld():
    print("hello world")
    print("hello", end=" ")  # 不换行的print
    print("world", end="")
    print("还剩余", 1, "元")  # 分割打印

def var():
    money = 50    # 变量定义方式
    print(type(money))

def type_conv():
    # 类型转换
    print(type(int("123")))
    print(type(str(123)))
    print(type(float("123.1")))

def calc_character():
    print("5 / 3 = ", 5 / 3)
    print("5 // 3 = ", 4 // 3)

def str():
    name = '黑马程序员'
    name = "黑马程序员"
    name = """黑马程序员"""   # 在变量时是字符串，单独放置是注释
    # 无法完成字符串和其他类型的拼接，字符串和其他类型的拼接要使用字符串格式化
    # name = "黑马程序员" + 1.0
    i = 10
    name = f"黑马程序员{i}"

def getInput():
    name = input("你是谁")
    print("我的名字是", name)

def boolean():
    result = True
    print(type(result))
    result = 10 > 5
    print(type(result))

    age = 10
    if age < 8:
        print("小孩")
    elif age < 18:
        print("未成年")
    else:
        print("成年")

def loop():
    # while循环
    current = 1
    sum = 0
    while(current <= 100):
        sum += current
        current += 1
    print(sum)

    # for循环
    name = "it黑马"
    for char in name:
        print(char)

    for i in range(5):
        print(i)

    for i in range(1, 5):
        print(i)

    for i in range(1, 5, 2):
        print(i)
