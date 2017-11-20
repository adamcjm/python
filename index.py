# -*- coding: utf-8 -*-
# name = input('please enter your name : ')
# print('my name is :', name)

# a = -100
# if a:
#     print(a)
# else:
#     print(-a)

# classmates = ['陈建明', '万康', '周杰伦', '张帅']
# print(classmates)

# classmates = ('陈建明', '万康', '周杰伦', '张帅')
# print(classmates)

# age = 17
# if age >= 18:
#     print('your age is :', age)
#     print('adult')
# else:
#     print('your age is :', age) 
#     print('teenager')

# age = 6
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# a = -1
# if a:
#     print(True)
# else:
#     print(False)

# birth = input('please enter your birth : ')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# names = ['Adam', 'Jhon', 'Lisa']
# for name in names:
#     print(name)

# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     sum += x
# print(sum)

# a = list(range(100))
# sum = 0
# print(a)
# for x in a:
#     sum += x
# print(sum)

# o = {'Adam': 100, 'Jhon': 90, 'Lisa': 80}
# print(o['Adam'])
# for x in o:
#     print(x, ':', o[x])
# print('qwe' in o)
# print(o.get('Mida', '不存在'))
# o.pop('Adam')
# print(o)

# s1 = set([1, 2, 3, 'Adam', 'Adam'])
# s2 = set([1, 'Adam', 'Jhon'])
# print(s1 & s2)
# print(s1 | s2)
# s1.add(4)
# print(s1)
# s1.remove("Adam")
# print(s1)

# a = ['c','b','a']
# b = [3,1,2]
# a.sort()
# b.sort()
# print(a,b)

# a = 'abc'
# a.replace('a','A')
# print(a)

# 函数
# print(abs(-100))
# print(max([1,4,7]))
# print(int(12.6))
# print(float(12))
# print(str(123))
# print(bool(0))
# print(bool(-1))
# print(bool(1))
# print(bool(''))
# print(hex(123))

# def my_abs(x):
#     if(x >= 0):
#         return x
#     else:
#         return -x
# a = -5
# print(my_abs(a))

# from myabs import myabs
# print(myabs(-100))

# def nop():
#     pass

# if age >= 18:
#     pass

# print(myabs('A'))
# print(abs('A'))

# def myabs(x):
#     if not isinstance(x, (int,float)):
#         raise TypeError('参数类型不是数字')
#     if x >= 0:
#         return x
#     else:
#         return -x
# myabs('A')

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
x, y = move(100, 200, 60, math.pi / 6)
print(x, y)
r = move(100, 200, 60, math.pi / 6)
print(r)

# next函数的参数
