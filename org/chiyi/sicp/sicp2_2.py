from operator import getitem


# 假设我们已经拥有一种从分子和分母中构造有理数的方式。
# 假设给定一个有理数，我们都有办法来提取它的分子和分母。
# 进一步假设，构造起和选择器以下面三个函数来提供
# make_rat(n,d) 返回分子为n和分母为d的有理数
# numer(x)返回有理数x的分子
# denom(x) 返回有理数x的分母


def add_rat(x, y):
    nx, dx = numer(x), denom(y)
    ny, dy = numer(y), denom(y)
    return make_rat(nx*dy+ny*dx, dx*dy)


def mul_rat(x, y):
    return make_rat(numer(x)*numer(y), denom(x)*denom(y))


def eq_rat(x, y):
    return numer(x)*denom(y) == numer(y)*denom(x)


# 使用元组表示有理数
from math import gcd

def make_rat(n, d):
    g = gcd(n,d)
    return (n//g, d//g)


def numer(x):
    return getitem(x, 0)


def denom(x):
    return getitem(x, 1)

# 打印有理数


def str_rat(x):
    """Return a string 'n/d' for numerator n and denominator d."""
    return '{0}/{1}'.format(numer(x), denom(x))


half = make_rat(1,2)
str_rat(half)
third = make_rat(1,3)
str_rat(mul_rat(half,third))
str_rat(add_rat(half,third))
