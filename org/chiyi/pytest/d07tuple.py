def main():
    # 定义元组
    t = ('test',38,True,'Test')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)

    # 错误：重新给元组赋值
    # t[0] = '1123'
    
    # 元组和列表互转
    person = list(t)
    print(person)
    fruits_list = ['apple','baanana','orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    

if __name__ == "__main__":
    main()