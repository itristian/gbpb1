################################## 1.
# a = ['tested', 13, 12.3, False, True]
# for a in a:
#     print(type(a))
################################## 2.
# i = 1
# inp = input()
# a = list(inp)
# print(f'', a, ' ---- ', len(a), 'elements')
# b = a.copy()
# llen = len(a)
#
# if llen % 2 == 0:
#     print('the list is even')
#     while i <= llen:
#         print(f'pair shuffle:', b[i-1],' and ', a[i])
#         b[i-1] = a[i]
#         b[i] = a[i-1]
#         i += 2
#     print(f'shuffled even list:', b)
# else:
#     print('the list is uneven')
#     while i < llen:
#         print(f'pair shuffle:', b[i - 1], ' and ', a[i])
#         b[i - 1] = a[i]
#         b[i] = a[i - 1]
#         i += 2
#     print('last symbol:', a[llen-1])
#     print(f'shuffled uneven list:', b)
################################# 3.
# month = int(input('month number: '))
# if 1 <= month <= 2 or month == 12:
#     month = 0
# elif 3 <= month <= 5:
#     month = 1
# elif 6 <= month <= 8:
#     month = 2
# else:
#     month = 3
# calendar = ['winter', 'spring', 'summer', 'autumn']
# print(f'the season of the month is', calendar[month])
################################## 4.
# a = input()
# b = a.split(" ")
# i = 0
# while i < len(b):
#     if len(b[i]) <= 10:
#         print(f'', b[i])
#     else:
#         c = (list(b[i]))
#         del c[10:len(c)]
#         c = [''.join(c[0:len(c)])]
#         print(f'', c[0])
#     i += 1
################################### 5.
# base = [7, 5, 3]
# new = int(input())
# if base.count(new) == 0:
#     if new >= base[0]:
#         base.insert(0, new)
#     else:
#         base.append(new)
#     base.sort(reverse=True)
# else:
#     base.insert(base.index(new), new)
# print(base)
#################################### 6.

products = [
    (1, {'name': 'printer', 'price': '3000', 'amount': '5'}),
    (2, {'name': 'fax', 'price': '5000', 'amount': '2'}),
    (3, {'name': 'paper', 'price': '100', 'amount': '17'}),
    (4, {'name': 'ink', 'price': '400', 'amount': '43'})
]
i_k = 0
i_r = 0
keys_list = list((products[0])[1].keys())
keys_amount = len(keys_list)
rows_amount = len(products)
info_list = list()
char = dict()

while i_k < keys_amount:
    while i_r < rows_amount:
        info_list.append(((products[i_r])[1]).get(keys_list[i_k]))
        i_r += 1
    char.update({keys_list[i_k]: info_list})
    info_list = list()
    i_r = 0
    i_k += 1
print(char)