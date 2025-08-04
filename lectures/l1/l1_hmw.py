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
print(', '.join(result1))
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
progrl1(st)
