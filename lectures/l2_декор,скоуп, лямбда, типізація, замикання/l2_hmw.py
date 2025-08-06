###########################################################
'''1) написати функцію (notebook) на замикання, котра буде в собі зберігати список справ,
вам потрібно реалізувати два методи:
– перший записує в список нову справу
– другий повертає всі записи
(приклад сигнатури функції notebook у вкладенні )'''
# from builtins import function
# from operator import indexOf

###########################################################
# def notebook():
#     what_to_list = []
#     def add_todo():
#         new_todo = input('нова справа -  ')
#         what_to_list.append(new_todo)
#     def get_all():
#         print('\nСписок справ')
#         for key, value in enumerate(what_to_list,1):
#             print(f'{key}.{value}')
#
#     return add_todo, get_all
# add, show = notebook()
# while True:
#     x=input('Обери, 1-додати . 2-показати . 3-вихід  :')
#     if x=='1':
#         add()
#     elif x=='2':
#         show()
#     elif x=='3':
#         break
#     else:
#         print('Неправильний вибір')
###########################################################
# from typing import Callable, Tuple
# def notebook()->Tuple[Callable[[],None], Callable[[],None]]:
#     what_to_list:list[str] = []
#     def add_todo()->None:
#         new_todo:str = input('нова справа -  ')
#         what_to_list.append(new_todo)
#     def get_all()->None:
#         print('\nСписок справ')
#         for key, value in enumerate(what_to_list,1):
#             print(f'{key}.{value}')
#
#     return add_todo, get_all
# add:Callable[[],None]
# show:Callable[[],None]
# add, show = notebook()
# while True:
#     x:str=input('Обери, 1-додати . 2-показати . 3-вихід  :')
#     if x=='1':
#         add()
#     elif x=='2':
#         show()
#     elif x=='3':
#         break
#     else:
#         print('Неправильний вибір')
###########################################################
'''2) протипізувати перше завдання'''
###########################################################

###########################################################
'''3) створити функцію, котра буде повертати суму розрядів числа у вигляді строки(також використовуємо типізацію)
Приклад:
expanded_form(12)  # return ’10 + 2′
expanded_form(42)  # return ’40 + 2′ 
expanded_form(70304)  # return ‘70000 + 300 + 4’'''
###########################################################
# from typing import Union
# number_user:Union[str,int] = input('Введіть число: ')
# def func_shower_n(task_list:Union[str, int])->str:
#     user_input:str = str(task_list)
#     result:list[str] =[]
#     for key,val in enumerate(user_input):
#         zeros:int = len(user_input) - key - 1
#         if val !='0':
#             result.append(val + "0"*zeros)
#     return ('+'.join(result))
# print(func_shower_n(number_user))

###########################################################
'''4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, 
та буде виводити це значення після виконання функцій приклад декоратору у вкладенні'''
###########################################################
# def decor(function):
#     count = 1
#     def inner(*args, **kwargs):
#         nonlocal count
#         print('*'*10 + ' count is = ' + str(count))
#         count += 1
#         function(*args, **kwargs)
#         print('-'*10)
#     return inner
#
# @decor
# def ex_f1():
#     print('First F')
# @decor
# def ex_f2():
#     print('Second F')
# @decor
# def ex_f3():
#     print('Third F')
# x = ex_f1(), ex_f2(), ex_f3(), ex_f1(), ex_f1(), ex_f2(), ex_f3()
