###########################################################
'''
Деструкторизація

 #1
 l = [1,2]
 a,b=l    \\ a=1,b=2
 #2
 l=[1,2,3,4,5]
 a,b,*_=l \\ a=1, b=2, _ = 3,4,5 (underscope)
 #3 list
 l = [1,2]
 def func(a,b):
    print(a,b)
func(*l) - *-means роспакувати
#4 dict
dict = {
'arg1':1,
'arg2':2,
}
func(*dict) - then we take only KEYS (arg1,arg2)
func(**dict) - then we take only VALUES (1,2)
'''
###########################################################
'''
# Декоратори
def decor(function):
    def inner(*args,**kwargs):   - арг и кваргс, для передачі аргументів
        print('*')
        function(*args,**kwargs)
        print('*')
    return inner
@decor   - працює з ближньою функцією
def greetion(name):
    print(f'Hello {name}')
'''
###########################################################
'''
Scope
1 - Global ||   2-Local (for function only)
global() local()
in function priority have local

def funct()
    def funct()
        nonlocal - не буде створювати змінну, перейде на 1 рівень вище, а ле не в глобал
        global - звернеться до глобальної змінної

'''
###########################################################
'''
Замикання
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
counter_2 = counter()
print(counter_2())
'''
###########################################################
'''
Лямда вирази
Якщо функція не має тіла, а лише повертає щось
funct = lambda a,b: a+b
map(lambda x: x**2, list) - повертає об'єкт генератор
filter(lambda x: x % 2 == 0, list) - повертає об'єкт генератор
'''
###########################################################
'''
Анотація типів 
def funct(name:list[str])->dict: (типізація для підказок, буде список Name в якому стрічки, а поверне дікт


import Typing (бібліотека)
from typing import Any, TypedDict, Callable - (для типізації функцій
User = TypedDict('User':str, 'name':int)
users:list[User]
'''

