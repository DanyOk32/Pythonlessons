# 1)
'''
Створити файл email.txt та наповнити його інформацію наступного формату (використайте для цього ШІ).
9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com
ec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i
44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com
ваша задача:  записати в новий файл тільки email’ /-ли з доменом gmail.com
'''



###############################################################################
'''def gmail_filter (file_name):
    result = []
    with open (file_name) as file1:
        for line in file1:
            if line.endswith('@gmail.com\n'):
                result.append(line)
    with open ('gmails_email.txt', 'w') as file2:
        file2.writelines(result)
gmail_filter('email.txt')

#'''##############################################################################
# 2)
'''
Створити записну книжку покупок:
– у покупки повинна бути id, назва і ціна
– всі покупки зберігаємо в файлі
 з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
 * має бути змога шукати по будь-якому полю покупку
 * має бути змога показати найдорожчу покупку
 * має бути можливість видаляти покупку по id
(ну і меню на це все)
'''
###############################################################################
''''def menu():
    print('1) - Вивід всіх покупок |      2) - Додати ')
    print('3) - Шукати             |      4) - Найдорожча покупка ')
    print('              5) - Видалити по ID')
    print('                  0) - Вихід   ')
# ---генератор айди
import json
def gen_id(width=5, iter_id=1):
    while True:
        yield f'{str(iter_id).zfill(width)}'
        iter_id += 1

id_purchase = gen_id()
class Purchase:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.purchase = []
    def open_file(self):
        try:
            with open(self.file_name) as file:
                self.purchase = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.purchase = []
    def write_to_file(self):
        try:
            with open(self.file_name, 'w') as file:
                json.dump(self.purchase, file, indent=4)
        except (Exception,):
            pass

    def adding(self):

        name = input('Name - ')
        while True:
            try:
                price = float(input('Price - '))
                break
            except ValueError:
                print('Invalid price, Must be Digit')
        new_purchase = {'id': next(id_purchase), 'name': name, 'price': price}
        self.purchase.append(new_purchase)
        self.write_to_file()
        input('Додано  :  ')
    def shower(self):
        self.open_file()
        if self.purchase:
            for one_purch in self.purchase:
                print(f'ID:{one_purch["id"]}, Name:{one_purch["name"]}, Price:{one_purch["price"]}$')
        else:
            print('No elements in notebook')

        input('Continue')

    def search(self):

        value = str(input('Пошук: '))
        self.open_file()
        found = False
        for one_purch in self.purchase:
            if value in one_purch['name'] or value in str(one_purch['price']):
                print(f'Name: {one_purch["name"]}, Price: {one_purch["price"]}')
                found = True
        if not found:
            print('No elements in notebook according to search')

        input('Back  - ')
    def max(self):
        self.open_file()
        result = max(self.purchase, key=lambda x: x['price'])
        input(f'Name: {result["name"]}             |              Price: {result["price"]}')
    def delete_by_id(self):
        while True:
            self.shower()
            self.open_file()
            try:
                choice_id = input('введіть айді (можна без нулів) -  ').zfill(5)
            except ValueError:
                print('Invalid Id, plese try again')
                continue
            found = False
            for lists in self.purchase:
                if lists['id'] == choice_id:
                    self.purchase.remove(lists)
                    self.write_to_file()
                    print('Deleted')
                    self.shower()
                    found = True
                    break
            if found:
                break
            else:
                print('No Id like this')
                input('Back:')





writer = Purchase('notebook.json')
while True:
    menu()
    choice = input('  Вибір  :   ')
    match choice:
        case '2':
            writer.adding()
        case '0' | False:
            break
        case '1':
            writer.shower()
        case '3':
            writer.search()
        case '4':
            writer.max()
        case '5':
            writer.delete_by_id()


'''
###############################################################################
# 3)
# '''
# Є ось такий список:
data = [
    [
        {'id': 1110, 'field': {}},
        {'id': 1112, 'field': {}},
        {'id': 1113, 'field': {}},
        {'id': 1114, 'field': {}},
        {'id': 1115, 'field': {}},
        {'id': 1111, 'field': {}},
    ],
    [
        {'id': 1110, 'field': {}},
        {'id': 1120, 'field': {}},
        {'id': 1122, 'field': {}},
        {'id': 1124, 'field': {}},
        {'id': 1125, 'field': {}},
    ],
    [
        {'id': 1130, 'field': {}},
        {'id': 1131, 'field': {}},
        {'id': 1122, 'field': {}},
        {'id': 1132, 'field': {}},
        {'id': 1133, 'field': {}},
    ]
]

def set_id_from_list(data_list):
    result = []
    gens=[(i['id'] for i in item if i['id'] not in result )for item in data_list]
    while gens:
        gen = gens.pop(0)
        try:
            result.append(next(gen))
            gens.append(gen)
        except StopIteration:
            pass
    return result


print(set_id_from_list(data))


    #
    # result_list2 = list_exemple.pop(0)
    # first_dict2 = result_list2.pop(0)
    # id_list.append(first_dict2['id'])
    # list_exemple.append(result_list2)
    #
    # result_list3 = list_exemple.pop(0)
    # first_dict3 = result_list3.pop(0)
    # id_list.append(first_dict3['id'])
    # list_exemple.append(result_list3)
    #
    # result_list4 = list_exemple.pop(0)
    # first_dict4 = result_list4.pop(0)
    # id_list.append(first_dict4['id'])
    # list_exemple.append(result_list4)
    #
    # result_list5 = list_exemple.pop(0)
    # first_dict5 = result_list5.pop(0)
    # id_list.append(first_dict5['id'])
    # list_exemple.append(result_list5)
    #
    # result_list6 = list_exemple.pop(0)
    # first_dict6 = result_list6.pop(0)
    # id_list.append(first_dict6['id'])
    # list_exemple.append(result_list6)




# print(next(result))
# print(next(result))
# print(next(result))





# def gen1(number):
#     for i in range(1, number+1):
#         yield f'{number}-Team1'
# def gen2(number):
#     for i in range(1, number+1):
#         yield f'{number}-Team2'
# teams=[gen1(5),gen2(7)]
# while teams:
#     team=teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration as e:
#     pass
# потрібно брати по черзі з кожного списку id і класти в список res.
# Якщо таке значення вже є в результуючому списку, то брати наступне з того ж підсписку
# з даним списком має вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, …….]
# '''
###############################################################################


