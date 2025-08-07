# class Shape:
#     def square(self):
#         print('ss')
#         return "square"
#     def perimeter(self):
#         print('perimeter')
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
# shape1 = Triangle(1, 2, 3)
# class TestingL3:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not isinstance (cls.__instance,cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __init__(self, home, number):
#         self.home = home
#         self.number = number
# user1 = TestingL3('buildin2', 123)
# user2 = TestingL3('buildin3', 123)
# print(user1.home)
# print(user2.home)
# class Array:
#     def __init__(self, *args):
#         self.__arr = [*args]
#     def __str__(self):
#         return str(self.__arr)
#     def __len__(self):
#         return len(self.__arr)
#     def __setitem__(self, index, value):
#         self.__arr[index] = value
#     def __getitem__(self, index):
#         return self.__arr[index]
#     def __delitem__(self, index):
#         del self.__arr[index]
#     def push(self, item):
#         self.__arr.append(item)
#     def map(self, func):
#         return Array(*[func(item) for item in self.__arr])
#     def filter(self, cb):
#         return Array(*[item for item in self.__arr if cb(item)])
# ===============================================
# from abc import ABC, abstractmethod
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         print('Hello')
# class Car(Transport):
#     def move(self):
#
# car = Car()
# car.move()
# ======================================================
'''
Создай абстрактный класс Animal, который:
имеет атрибут name;
содержит абстрактный метод make_sound().
Создай классы-наследники:
Cow → звук: "Moo"
Dog → звук: "Woof"
Chicken → звук: "Cluck"
Создай список разных животных (экземпляры классов Cow, Dog, Chicken), и пройдись по нему циклом, вызывая make_sound() для каждого.

Bobby says: Moo
Rex says: Woof
Chika says: Cluck
'''
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Cow(Animal):
#     def make_sound(self):
#         print(f'{self.name} says: Moo')
# class Dog(Animal):
#     def make_sound(self):
#         print(f'{self.name} says: Woof')
# class Cluck(Animal):
#     def make_sound(self):
#         print(f'{self.name} says: Cluck')
# cow1 = Cow('Olga1')
# dog1 = Dog('oleg1')
# cow2 = Cow('Olga2')
# cluck1 = Cluck('Ryaba')
# animal_list = [cow1, dog1, cluck1]
# for i in animal_list: i.make_sound()
