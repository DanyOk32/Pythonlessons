"""
1) написати прогу, яка вибирає зі введеної строки цифри і виводить їх через кому,
#
# наприклад:
#
# st = ‘as 23 fdfdg544’ введена строка
#
# 2,3,5,4,4        #вивело в консолі.
"""


###########################################################
st = 'as 12 fsad124 4124dsf 1234f'
result1 =[j for j in st if j.isdigit()]
# print(', '.join(result1))
###########################################################
"""
2)написати прогу, яка вибирає зі введеної строки числа і виводить їх так, як вони написані

наприклад:

  st = ‘as 23 fdfdg544 34’ #введена строка

  23, 544, 34              #вивело в консолі

"""
###########################################################
def progrl1(string_ex):
    result2 = []
    number = ''
    for i in string_ex:
        if i.isdigit():
            number += i
        else:
            if number:
                result2.append(number)
                number = ''
    if number:
        result2.append(number)
    print(', '.join(result2))
    # print(sum(int(k) for k in result2))



st = 'as 23 fdfdg544 34'
# print(', '.join(''.join([ch if ch.isdigit() else ' ' for ch in st]).split()))
# print(''.join([ch if ch.isdigit() else ' ' for ch in st]).split())
# progrl1(st)

###########################################################
'''1) є
строка:

greeting = ‘Hello, world’

записати кожний символ, як окремий елемент списку, і зробити його заглавним:

[‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘, ’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’]'''
###########################################################
greeting = 'Hello, world'
# print([k.upper() for k in greeting])
###########################################################
'''2) з діапазону від 0-50 записати тільки непарні числа, при цьому піднести їх до квадрату

приклад:

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, …]'''
###########################################################
# print([i**2 for i in range(50) if i%2==0])
# print([i for i in range(10, 101) if i%2==1 and i*2%5==0])


###########################################################
'''function
– створити функцію, яка виводить List +
– створити функцію, яка приймає три числа, та виводить та повертає найбільше. +
– створити функцію, яка приймає будь - яку кількість чисел, повертає найменше, а виводить найбільше +
– створити функцію, яка повертає найбільше число з List +
– створити функцію, яка повертає найменше число з'''
###########################################################
def function_shower(numbers):
    print(numbers)
def function_tsk2(a,b,c):
    print(max(int(a),int(b),int(c)))
    return max(int(a),int(b),int(c))
def function_tsk3(*args):
    print(max(args))
    return min(args)
def function_tsk4(List):
    print(max(List))
# function_tsk4([1,2,3,4,5,6])
def fucntion_tsk5(*args):
    print(min(args))
###########################################################
'''List
– створити функцію, яка приймає List чисел та складає значення елементів List та повертає його.
– створити функцію, яка приймає List чисел та повертає середнє арифметичне його значень.'''
###########################################################
def function_2_tsk1(List):
    print(sum(List))
    return sum(List)
# function_2_tsk1([1,2,3,4,5,6])
def function_2_tsk2(List):
    print(sum(List)/len(List))
    return sum(List)/len(List)


# function_2_tsk2([1,2,3,4,5,6])
###########################################################
"""
1 Є list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  – знайти  мін. число
  – видалити усі дублікати
  – замінити кожне 4-те значення на ‘X’
2) вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції
3) вивести табличку множення за допомогою циклу while
4) переробити це завдання під меню
"""
###########################################################
list_tsk3 = [22, 3,5,2,8,2,-23, 8,23,5]
# print(min(list_tsk3))
list_tsk3_new=list(set(list_tsk3))
# print(list_tsk3_new)
def replaced_Every_fourth(list):
    return ['x' if i%4==0 else value for i,value in enumerate(list) ]
# print(replaced_Every_fourth(list_tsk3))
def stranno(x):
    i=1
    while i <= x:
        if i ==1 or i ==x:
            print('*'*x)
        else :
            print('*' + ' '*(x-2) + '*')
        i+=1
# stranno(15)
def table_calc ():
    integer =1
    while integer < 10:
        multipl = 1
        while multipl < 10:
            print(f'{integer:2} * {multipl:1} = {integer*multipl:3}', end=' ')
            multipl += 1
        print()
        integer += 1
def menu_Fun():
    while True:
        print('1) - min число')
        print('2) - дублікати')
        print('3) - видалити кожне 4те')
        print('4) - квадрат зі стороною')
        print('5) - множення табл')
        print('6) - EXIT')
        result = input()
        if result == '1':
            print(f'min число це {min(list_tsk3)}')
        elif result == '2':
            print(set(list_tsk3))
        elif result == '3':
            print(replaced_Every_fourth(list_tsk3))
        elif result == '4':
            stranno(15)
        elif result == '5':
            table_calc()
        elif result == '6':
            'break'
        else: 'поганий вибір'
menu_Fun()