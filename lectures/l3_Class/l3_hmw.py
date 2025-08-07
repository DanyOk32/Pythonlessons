###############################################################################
'''
Створити клас Rectangle:
-він має приймати дві сторони x,y
Описати поведінку арифметичним методом:
  + сума площин двох екземплярів класу
  – різниця площин двох екземплярів класу
  == площин на рівність
  != площин на нерівність
  >, < менше більше
  при виклику метода len() підраховувати суму сторін
'''
###############################################################################
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
#     def __add__(self, other):
#         return self.area() + other.area()
#     def __sub__(self, other):
#         return self.area() - other.area()
#     def __eq__(self, other):
#         return self.area() == other.area()
#     def __lt__(self, other):
#         return self.area() < other.area()
#     def __gt__(self, other):
#         return self.area() > other.area()
#     def __len__(self):
#         return self.x + self.y
# Shape1 = Rectangle(3,4)
# Shape2 = Rectangle(2,5)
# print(Shape1.__len__())
# print(Shape1.__eq__(Shape2))
# print(Shape1.__add__(Shape2))
#

###############################################################################
'''
створити клас Human (name, age)
створити два класи Prince и Cinderella, які наслідуються від Human:
у попелюшки має бути ім’я, вік, розмір ноги
у принца має бути ім’я, вік, та розмір знайденого черевичка, а також метод, котрий буде приймати список попелюшок, 
та шукати ту саму в класі попелюшки має бути count, який буде зберігати кількість створених екземплярів класу
також має бути метод класу, який буде виводити це значення
'''
###############################################################################
# class Human:
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
# class Cinderella(Human):
#     count = 0
#     def __init__(self, name, age, foot_s:int):
#         super().__init__(name, age)
#         self.foot_s = foot_s
#         Cinderella.count += 1
#
#     @classmethod
#     def show_count(cls):
#         return cls.count
# class Prince(Human):
#     def __init__(self, name, age, found_sh:int):
#         super().__init__(name, age)
#         self.found_sh = found_sh
#
#     def cinderella_finder(self, cinderellas:list[Cinderella])->list[Cinderella] | None:
#         counter_cinderellas:list[Cinderella] = []
#         for girl in cinderellas:
#             if girl.foot_s == self.found_sh:
#                 counter_cinderellas.append(girl)
#
#         return counter_cinderellas
# prince1 = Prince('Prince1', 10, 5)
# princess1 = Cinderella('ivanka', 5, 5)
# princess2 = Cinderella('Princess2', 5, 8)
# princess3 = Cinderella('zina', 5, 5)
# princess4 = Cinderella('Princess3', 5, 5)
# princess5 = Cinderella('olga', 8, 10)
# # print(Cinderella.show_count())
# finder = prince1.cinderella_finder([princess2, princess3, princess1,princess5, princess4 ])
# for find_c in finder:
#     print(f'{find_c.name} ------ {find_c.foot_s}')
# print('all', Cinderella.show_count())

###############################################################################

'''1) Створити абстрактний клас Printable, який буде описувати абстрактний метод print() +
2) Створити класи Book та Magazine, в кожного в конструкторі змінна name, та який наслідується від класу Printable +
3) Створити клас Main, в якому буде:
– змінна класу printable_list, яка буде зберігати книжки та журнали
– метод add, за допомогою якого можна додавати екземпляри класів в список і робити перевірку, чи то
що передають, є класом Book або Magazine інакше ігнорувати додавання
– метод show_all_magazines, який буде виводити всі журнали, викликаючи метод print абстрактного класу
– метод show_all_books, який буде виводити всі книги, викликаючи метод print абстрактного класу'''
########
'''Приклад:
Main.add(Magazine(‘Magazine1’))
Main.add(Book(‘Book1’))
Main.add(Magazine(‘Magazine3’))
Main.add(Magazine(‘Magazine2’))
Main.add(Book(‘Book2’))
Main.show_all_magazines()
print(‘-‘ *40)
Main.show_all_books()
для перевірки класів використовуємо метод isinstance, приклад:
user = User(‘Max’, 15)
shape = Shape()
isinstance(max, User) -> True
isinstance(shape, User) -> False'''
###############################################################################
# from abc import ABC, abstractmethod
# class Printable(ABC):
#     def __init__(self, name:str):
#         self.name = name
#     @abstractmethod
#     def print(self):
#         pass
# class Book(Printable):
#     def print(self):
#         print('Book - '+ self.name)
# class Magazine(Printable):
#     def print(self):
#         print('Magazine - '+ self.name)
# class Main:
#     printable_list:list[Printable] = []
#
#     @classmethod
#     def add(cls, value):
#         if isinstance(value, (Book, Magazine)):
#             cls.printable_list.append(value)
#
#     @classmethod
#     def show_all_magazines(cls):
#         for item in cls.printable_list:
#             if isinstance(item, Magazine):
#                 item.print()
#     @classmethod
#     def show_all_books(cls):
#         for item in cls.printable_list:
#             if isinstance(item, Book):
#                 item.print()
#
#
# Main.add(Magazine('Magazine 11111'))
# Main.add(Book('Kniga gggg'))
# Main.add(Book('12333 ggKNgg'))
# Main.add(Magazine('Magazine fff'))
# Main.add(Magazine('Magazine 22222'))
# Main.show_all_magazines()
# Main.show_all_books()
#


