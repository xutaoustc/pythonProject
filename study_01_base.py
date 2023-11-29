# 数字
#   整数 - 没有long类型
#   浮点数
#   布尔
# 非数字
#   字符串
#   列表 - 有序可变序列
#   元组 - 有序不可变序列
#   集合 - 无序不重复集合
#   字典


"""
this is a comment
"""

def helloWorld():
    print("hello world")
    # 分割打印
    print("还剩余", 1, "元")
    # 不换行的print
    print("hello", end=" ")
    print("world", end="")

def var():
    # 变量名 = 变量值  完成变量定义
    money = 50
    # 变量类型
    print(type(money))
    # 类型转换
    print(type(int("123")))
    print(type(str(123)))
    print(type(float("123.1")))
    # Bool类型
    result = True
    print(type(result))
    result = 10 > 5
    print(type(result))
    # 变量没有类型！

def calc_character():
    print("5 / 3 = ", 5 / 3)      # 计算小数位
    print("5 // 3 = ", 4 // 3)    # 取整除

def str():
    name = '黑马程序员'
    name = "黑马程序员"
    name = """黑马程序员"""   # 用变量接收是字符串，单独放置是注释
    # +号字符串拼接： 可以完成字符串和字符串之间的拼接； 但无法完成字符串和其他类型的拼接，name = "黑马程序员" + 1.0
    # 字符串格式化拼接：字符串和其他类型的拼接要使用字符串格式化
    i = 10
    name = f"黑马程序员{i}"

def getInput():
    name = input("你是谁")
    print("我的名字是", name)

def if_else():
    age = 10
    if age < 8:
        print("小孩")
    elif age < 18:
        print("未成年")
    else:
        print("成年")

    # and or not
    if age <10 and age > 5:
        print("child")
    elif age > 10 or age < 20:
        print("child1")
    elif not age > 30:
        print("child2")

def while_test():
    current = 1
    sum = 0
    while(current <= 100):
        sum += current
        current += 1
    print(sum)

def for_test():
    name = "it黑马"
    for char in name:
        print(char)

    for i in range(5):
        print(i)

    for i in range(1, 5):
        print(i)

    for i in range(1, 5, 2):
        print(i)
