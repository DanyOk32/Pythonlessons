# name = 'alex'
# x = '1'
# def funct():
#     name = 'annya'
#     print(name)
#     print(x)
# funct()
# --------------------------------------------------------
# name = 'oleg'
# def funct():
#     name = 'petya'
#     def funct2():
#         # nonlocal name
#         # global name
#         name = 'sonya'
#         print(name)
#     funct2()
#     print(name)
# funct()
# print(name)
# --------------------------------------------------------
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# counter_2 = counter()
# print(counter_2())
# print(counter_2())
# print(counter_2())
# --------------------------------------------------------
# list_exemple=[1,2,3,4,5]
# print(list(map(lambda x: x ** 2, list_exemple)))
# print(list(filter(lambda x: x % 2 == 0, list_exemple)))

# -------
# from typing import Callable
# def make_counter(a:str, b:int)->Callable[[str, bool],int]:
#     count = 0
#     def inner(z:str, y:bool)->int:
#         nonlocal count
#         count += 1
#         return count
#     return inner
# counter = make_counter('s',2)
# print(counter('s',True))
# print(counter('s',True))
# print(counter('s',True))
# -------
# def remember_last():
#     first = None
#     def inner():
#         nonlocal first
#         print(f'Предыдущее значение {str(first):5}')
#         second = input("Введите Новое значение ")
#         first = second
#     return inner
# bbb=remember_last()
# print(bbb())
# print(bbb())
# print(bbb())
# print(bbb())
# -------213
result=''
x=input('sd      1 ')
i=1
for key in x:
    z = len(x) - i
    if i!=len(x):
        result = result + key + '0'*z + ' + '
    elif i==len(x):
        result = result + key + '0'*z
    i+=1
print(result)

