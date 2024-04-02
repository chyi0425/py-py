#!/usr/bin/python3
# _*_ coding: utf-8 _*_

def for_loop(n: int) -> int:
    """ for 循环 """
    res = 0
    # 循环求和 1,2,...,n-1,n
    for i in range(1, n + 1):
        res += i
    return res


def while_loop(n: int) -> int:
    """ while 循环 """
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res


def while_loop_ii(n: int)-> int:
    """ while loop twice renew"""
    res = 0
    i = 1
    while i<=n:
        res +=i
        # 更新条件变量
        i += 1
        i *= 2
    return res

def nested_for_loop(n: int) -> str:
    """ double for loop"""
    res = ""
    for i in range(1, n+1):
        for j in range (1, n+1):
            res += f"({i},{j}),"
    return res

if __name__ == "__main__":
    n=5
    res = nested_for_loop(n)
    print(f"\n双层 for 循环的遍历结果{res}")