def list_test():
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