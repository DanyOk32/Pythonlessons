# g = (i for i in range(1_000_000))
# for i in g:
#     print(i)
# --------------
''' - функція запису всяких імейлів, але з фільтром Гмаіл
def email_writer(filename:str):
    pattern = '@gmail.com'
    if filename.endswith(pattern):
        with open('email.txt', 'a') as file:
            file.write(f'{filename}\n')
email_writer('12412414214141 1421241 2412 41 24@gmail.com')
email_writer('12412414214141 1421241 2412 41 24@mail.com')
email_writer('12@gmail.com')
email_writer('13@gmail.com')
'''
# def email_writer(filename:str):
#     pattern = '@gmail.com'
#     if filename.endswith(pattern):
#         with open('email.txt', 'a') as file:
#             file.write(f'{filename}\n')
# email_writer('12412414214141 1421241 2412 41 24@gmail.com')
# email_writer('12412414214141 1421241 2412 41 24@mail.com')
# email_writer('12@gmail.com')
# email_writer('13@gmail.com')

# def sort_file(filename):
#     list_for_file = []
#     with open(filename, 'r') as file:
#         files_list = str(file.read()).split('\n')
#         print(files_list)
#         for email in files_list:
#             if str(email).endswith('@gmail.com'):
#                 list_for_file.append(f'{email}\n')
#         print(list_for_file)
#     with open('result_email.txt', 'w') as file2:
#         for emails in list_for_file:
#             file2.write(emails)
# -----------\---------------------------------------
#     result = []
# with open('email.txt', 'r') as file:
#     for line in file:
#         if line.endswith('@gmail.com\n'):
#             # print(line)
#             result.append(line)
# # print(result)
# with open ('result_email.txt', 'w') as file2:
#     file2.writelines(result )
#




    # with open('result_email.txt', 'w') as result_file:
    #     for iterator_list in list_for_file:
    #         result_file.write(f'{iterator_list}\n')


# sort_file('email.txt')
# __________________________________
#
#
# import json
# from typing import TypedDict
#
# result=TypedDict('result',{'name':str, 'price': float, 'id': int})
#
# notebook_list=[]
# def show_menu():
#     print('Menuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
#     print('1- Add Buy  |  2- Del Buy by id')
#     print('3- Show Buy  |  4- Max Value Buy')
#     print('5- Search Value Buy  |  0- Exit')
# id_staff = 0
# def add_st():
#     global id_staff
#     name_buy = input('Enter name of buy:  ')
#     try :
#         price_buy = float(input('Enter price of buy:  '))
#         dict_add = {'name': name_buy, 'price': price_buy, 'id': id_staff}
#         notebook_list.append(dict_add)
#         id_staff += 1
#         with open('results.json', 'w') as file:
#             json.dump(notebook_list, file)
#     except ValueError:
#         print('Price must be Value')
#
# def del_by_id():
#     try:
#         id_user = int(input('Enter id of user:  '))
#         for item in notebook_list:
#             if item.get('id') == id_user:
#                 notebook_list.remove(item)
#                 print('deleted')
#                 break
#         else:
#             print('Not found')
#     except ValueError:
#         print('Id must be Value')
#     input('Back')
# def show_notebook():
#     with open('results.json', 'r') as file:
#         notebook_list2 = json.load(file)
#         for data in notebook_list2:
#             print(f'Name: {data['name']} , Price: {data['price']} , Id: {data['id']}')
#     input('Back')
# def search_value():
#     value = input('Enter value to search:  ')
#     result_of_search=[]
#     for item in notebook_list:
#         choice_name = item.get('name')
#         if choice_name == value:
#             result_of_search.append(item)
#     if result_of_search:
#         print(result_of_search)
#     else:
#         print('Not found')
#     input('Back')
# def max_price():
#     list_price = []
#     for item in notebook_list:
#         list_price.append(item.get('price'))
#     for item2 in notebook_list:
#         if item2.get('price') == max(list_price):
#             print(item2)
#     input('Back')
#
#
# while True:
#     show_menu()
#     choice = input('Enter your choice: ')
#     if choice == '1':
#         add_st()
#     elif choice == '2':
#         del_by_id()
#     elif choice == '3':
#         show_notebook()
#     elif choice == '4':
#         max_price()
#     elif choice == '5':
#         search_value()
#     elif choice == '0' or False:
#         break
#---------------------------------------------
def gen_id_purch(start=0, width=5):
    while True:
        yield f'{str(start).zfill(width)}'
        start += 1
gen_id = gen_id_purch()
print(next(gen_id))
print(next(gen_id))
print(next(gen_id))
print(next(gen_id))
