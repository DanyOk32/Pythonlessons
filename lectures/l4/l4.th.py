###########################################################
# Debuger, iterators, Generators, Files, some bibloitecs, PatternMatch
###########################################################
# --------Debugger
# breakpoint
# --------Errors
'''
try:
    ....
except 'key'Error as e:    - if error\ignore it
    print('fixed', e)    - e-error sentence
except Exception - all error
else:
    ... - якщо не буде помилок
finally:
   ... - в любому разі спрацює
'''
from email.policy import default

###########################################################
# -------Generators
'''
l = [i for i in range(50_000_000)]
g =(i for i in range(50_000_000))
print(next(g))
-на останній буде  помилка
 ---exemple-----------------------------------
def gen():
    yield 1
    yield 2
    yield 3
    return 'smthing'
g = gen()
try:
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)
---exemple----------------------------------------
'''
# Приклад з командами, послідовно, та з генератором
'''
def gen1(number):
    for i in range(1, number+1):
        yield f'{number}-Team1'
def gen2(number):
    for i in range(1, number+1):
        yield f'{number}-Team2'
teams=[gen1(5),gen2(7)]
while teams:
    team=teams.pop(0)
    try:
        print(next(team))
        teams.append(team)
    except StopIteration as e:
    pass
'''
###########################################################
'''import uuid     - генератор назви файлу
def gen_jpg_file():
    pattern = '{}.jpg'
    while True:
        yield pattern.format(uuid.uuid4())
file_gen = gen_jpg_file()
print(next(file_gen))'''
# iterator
# class nnn:
#     ...
#     def __iter__(self):
#         return self
#     def __next__(self):
#         ......
#
# generator:
# def funct():
#     ....
#     yield
###########################################################
'''files'''
########
'''file = open('....', mode='r' (Read), - якщо файла немає - помилка)
print(file.read())
file.close()   -обовязково
try:
    with open('...') as file:
        print(file.read())
        print([file.read()])
        print(file.readline())
        print(file.readlines())
        for line in file:
            print()
except Exception as e:   (Exception,)
    print(e)
'''
# Режими:
'''r - read(default) also have rb (binary), w-write, a-append, х-створення файлу, w+-write and read, r+ - 
file.write('....\n....\n) - перетре файл, або створить
with open('...', 'a') as file:
    file.write('...') - додасть щось
with open('...', 'x') as file:
    pass  - створить файл, або дасть помилкку, якщо такий вже існує
file.seek(0) - передвине курсор в файлі
'''
# Бібліотеки
'''
import json
import pickle (binary)
-записати в json
++++++++++++++++++++++++++++++++++++++++++++++++++++++
User = TypedDict('User',{'name':str,'age':int})
users:list[User] = [
    {'name':'Max', 'age': 15}
    {'name':'Olga', 'age': 13}
]
try:
    with open('users.json', 'w') as file:   || 'w' - 'r'  - записування(створення)
    json.dump(users, file)                  || .dumb(users, file) - .load(file)   - читання
except Exception as e:
    print(e)
++++++++++++++++++++++++++++++++++++++++++++++++++++++
pickle - режими ті ж самі, замість json - pickle    'w' - 'wb' | 'r' - 'rb'
'''
# PatterMatch
'''
x = input('Any')
match x:
    case 'no':
        do smthig
    case _:  -default
--in class
__match_args__ = ('...', '...') - для match
++++++
def matcher(source:className,dict):
    if isinstance(source,className):
        ....
    if isinstance(source,dict):
    ....
------EXEMPLES
def matcher (source:className,dict):
    match source:
        case className(...,...):
            ...
        case {'...': .... , '...': ...}:
        ...
'''