###########################################################
# Класи
###########################################################
'''
CamelCase

class User:    =  class User(object):
    count = 0
    def __init__(self, name,age):   (конструктор)
        self.name = name   || self.__name - скрите
        self.age = age     || self._age - приватне
    def __str__(self):      (метод для стрічки) - щоб не повертало адрессу
        return(f'{self.name},{self.age}')
    def __repr__(self): - метод коли ми створимо в два юзера в одному лісті. Тоді репр(те саме що стр)
    __dict__ - перетворить на словник
    ex. return(self.__dict__)

    __slots__('name', 'age') - які поля дозволені. Для запобігання додавання нових полів

 user1 = User('Alex',88) - сконструє по классу

 ----------------------------
 наслідування класів, Extended
 class User_N(User): - (в дужках наслідування)
    def __init__ (Alt+Enter)(self, name, age - унаслідуванні класи,  + свої класи):
        super().__init__(name, age)
        self.свої класи = свої класи'
    CTRL + O, відкриє все унаслідування

    Абстрактні класи - это шаблон для других классов.
    Он не предназначен для создания экземпляров, а только для наследования.

    from abc import ABC, abstractmethod
    class name(ABS):
    @abstractmethod - декоратор,ОБОВ'ЯЗКОВИЙ,
    def pay(self, amount)
        pass
    class exemple2(pay) - унаслідує абстрактний клас pay
    -використувується для стандартизації

    Інкапсуляція
    @property - дозволяє користуватись функцією як атрибутом
    def give(self)
        return self.price

    -Поліморфізм
    -ClassMethod
    @classmethod
    def func(not SELF, but slc) - Теперь можна викликати фунцію через клас, а не через екзмепляр
    @staticmethod - аналогічно, можна через екземпляр, можно через клас
    def func()
        print('heelll)
    -Перегрузка методів 'Overload'
    from typing import Self - для типізації other
    def __add__(self, other:Self)
    def __sub__(self, other:Self)
    def __mul__(self, other:Self)
    def __len__(self):
    __new__(cls, *args, **kwargs): - спочатку реалізується цей метод, та керує конструктором (SINGLETON)
    __call__(cls,value) - Дозволяє зробити єкземпляр класу, як фунцію, якщо її викликати
        self.age+=value -приклад

-----------------------------------------
class Array:
    def __init__(self, *args):
        self.__arr = [*args]
    def __str__(self):
        return str(self.__arr)
    def __len__(self):
        return len(self.__arr)
    def __setitem__(self, index, value):
        self.__arr[index] = value
    def __getitem__(self, index):
        return self.__arr[index]
    def __delitem__(self, index):
        del self.__arr[index]
    def push(self, item):
        self.__arr.append(item)
    def map(self, func):
        return Array(*[func(item) for item in self.__arr])
    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])

'''