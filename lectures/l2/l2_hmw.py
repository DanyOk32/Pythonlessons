###########################################################
'''1) написати функцію (notebook) на замикання, котра буде в собі зберігати список справ,
вам потрібно реалізувати два методи:
– перший записує в список нову справу
– другий повертає всі записи
(приклад сигнатури функції notebook у вкладенні )'''
from operator import indexOf

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
number_user = input('Введіть число: ')
def expanded_form(us_nmb):
    result = ''
    for key, values in enumerate(us_nmb,1):

        if key !=len(us_nmb) and values !=0:
            result = result + values + '0'*int(len(us_nmb)-key) + ' + '
        elif key ==len(us_nmb) and values !=0:
            result = result + values + '0'*int(len(us_nmb)-key)
    print(result)
expanded_form(number_user)
###########################################################
'''4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, 
та буде виводити це значення після виконання функцій приклад декоратору у вкладенні'''
###########################################################

