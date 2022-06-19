#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @author : chiyi
# @desc : 兔子产子问题

if __name__ == "__main__":
    fib1 = 1
    fib2 = 1
    i = 3
    # 输出第一个月和第二个月的兔子对数
    print("%6d      %6d" % (fib1, fib2), end="     ")
    while i <= 30:
        fib = fib1 + fib2
        # 迭代求出当前月份的兔子对数
        print("%6d" % fib, end="        ")
        if i % 4 == 0:
            print()  # 每行输出4个
        fib2 = fib1
        fib1 = fib
        i += 1
