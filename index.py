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

# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx,ny
# x, y = move(100, 200, 60, math.pi / 6)
# print(x, y)
# r = move(100, 200, 60, math.pi / 6)
# print(r)

# 函数的参数
# 位置参数
# def power(x):
#     return x * x
# print(power(10))

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))

# def enroll(name, gender, age=6, city='上海'):
#     print(name,'性别：',gender, ',年龄：', age, ',来自', city, '.')
# enroll('杨', '男', 18, '北京')

# def add_end(L= []):
#     L.append('end')
#     return L
# print(add_end())
# print(add_end())

# def add_end(L = None):
#     if L is None:
#         L = []
#     L.append('end')
#     return L
# print(add_end())
# print(add_end())
# print(add_end())

# for x in [1,2,3,4]:
#     print(x)

# sum = 0
# n = 99
# while n > 0:
#     n -= 2
#     sum += n
# print(sum)
# print(n)

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     print(sum)
# calc(*[1,2,3,4])
# calc(1,2,3,4)

# def person(name, age, **kw):
#     print(name)
#     print(age)
#     print(kw)
# # person('Adam', 10, city='sh', gender = 'nan')
# a = {'city': 'sh', 'gender': 'nan'}
# # person('Adam', 15, **a)
# person('Jhon', 18, city=a['city'], gender=a['gender'])
# person('Lisa', 20, **a)

# def person(name, age, **kw):
#     if 'city' in kw:
#         print('yes-city')
#         pass
#     if 'gender' in kw:
#         print('yes-gender')
#         pass
# # person('Adam', 6, city='sh')
# a = {'city': 'sh', 'gender': 'f'}
# person('Jhon', 1, **a)
