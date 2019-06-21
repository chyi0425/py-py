from random import randint


def roll_dice(n=2):
    """
    掷骰子

    :param n: 骰子的个数
    :return: n颗骰子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a+b+c


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1, 2))
print(add(c=50, a=100, b=300))

def add(*args):
    total = 0
    for val in args:
        total +=val
    return total

print(add(1,3,4,5,6,33,7,8))

from module1 import foo

foo()

from module2 import foo
foo()

import module1 as m1
import module2 as m2

m1.foo()

m2.foo()