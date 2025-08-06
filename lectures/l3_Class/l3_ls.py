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

