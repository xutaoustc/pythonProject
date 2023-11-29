# 非数字
#   字符串
#   列表 - 有序可变序列（*在其他语言中通常叫数组）
#   元组 - 有序不可变序列
#   集合 - 无序不重复集合
#   字典

# 所有非数字类型变量都有以下特点：
#   都是一个序列sequence，可以理解为容器
#   取值[]
#   遍历for in
#   计算长度、最大/最小值、比较、删除
#   链接+和重复*
#   切片

def list_test():
    """
    增加： insert
          append
          extend
    删除： del
          remove
          pop
          pop()
          clear
    取值，取索引：
          下标
          index
    统计： len
          count
    排序： sort
          reverse
    :return:
    """
    # 列表中存储的类型可以是不同的数据类型
    my_list = ["1", "2", "3"]
    my_list_1 = ["1", 2, True]

    # 下标访问
    element = my_list[0]
    element = my_list[-1]
    # 修改
    my_list[1] = "22"

    # 获取元素的下标，如果找不到则报错
    index = my_list.index("3")
    print(index)

    # insert, append, extend
    my_list.insert(1, "ins")
    my_list.append("4")
    my_list.extend(["ao", "li", "gei"])
    print(my_list)

    # delete, pop, remove, clear
    del my_list[1]
    pop_element = my_list.pop(1)
    my_list.remove("ao")  # 删除第一个匹配的项
    my_list.clear()

    # 统计某元素在列表内的数量
    my_list.count("li")

    # 统计列表元素数量
    print(len(my_list))

list_test()