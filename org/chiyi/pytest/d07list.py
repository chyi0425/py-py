def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello']*5
    print(list2)

    # 计算列表的长度
    print(len(list1))
    #下标运算
    print(list1[0])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    list1[2]=300
    print(list1)
    # 添加元素
    list1.append(200)
    list1.insert(1,400)
    list1 +=[1000,2000]
    print(list1)
    print(len(list1))
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
    list1.clear()
    print(list1)

    # 和字符串一样，列表也可以做切片操作，通过切片操作，我们可以实现对列表的复制或者将列表中的一部分取出来创建新的列表

    fruits = ['grape','apple','strawberry','waxberry']
    fruits += ['pitaya','pear','mango']
    # 循环便利列表元素

    for fruit in fruits:
        print(fruit.title,end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

    # 下面的代码实现了对列表的排序串操作
    fruits5 = sorted(fruits)
    fruits6 = sorted(fruits,reverse=True)
    fruits7 = sorted(fruits,key=len)
    print(fruits)
    print(fruits5)
    print(fruits6)
    print(fruits7)

    # 直接对列表本身进行排序
    fruits.sort(reverse=True)
    print(fruits)

    # 我们还可以使用生成式语法来创建列表
    import sys
    f = [x for x in range(1,10)]
    print(f)
    f=[x+y for x in 'ABCDE' for y in '1234567']
    print(f)

    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1,1000))
    print(sys.getsizeof(f)) # 相比生成式，生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)

if __name__ == "__main__":
    main()