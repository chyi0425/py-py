"""
英制单位英寸和公制单位厘米互换
"""

import math
from random import randint
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value/2.54))
else:
    print('请输入有效的单位')


"""
掷骰子决定做什么事情
"""


face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
elif:
    result = '讲冷笑话'


"""
判断输入的边长能否构成三角形
"""


a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a+b > c and a+c > b and b+c > a:
    print('周长:%f' % (a+b+c))
    p = （a+b+c)/2
    area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积:%f' % (area))
else:
    print('不能构成三角形')