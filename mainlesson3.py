###################################################### 1.
# def division(n1, n2):
#     result = int(n1) / int(n2)
#     return result
#
#
# num1 = input('first number')
# num2 = input('second number')
# print(division(num1, num2))
###################################################### 2.
# def rowmaker():
#     name = input('name')
#     surname = input('surname')
#     bd = input('date')
#     address = input('address')
#     email = input('email')
#     phone = input('phone')
#     print(f'', name, surname, bd, address, email, phone)
#
#
# rowmaker()
###################################################### 3.
# def my_func(arg1, arg2, arg3):
#     arglist = [arg1, arg2, arg3]
#     arglist.sort(reverse=True)
#     result = arglist[0] + arglist[1]
#     return result
#
#
# a1 = int(input('first argument '))
# a2 = int(input('second argument '))
# a3 = int(input('third argument '))
# print(my_func(a1, a2, a3))
###################################################### 4.
# def my_fun(arg1base, arg2):
#     arg2pos = -arg2
#     arg1 = arg1base
#     i = 1
#     while i < arg2pos:
#         arg1 = arg1base*arg1
#         i += 1
#     arg1 = 1 / arg1
#     return arg1
#
#
# x = int(input('first number '))
# y = int(input('second number '))
# print(my_fun(x, y))
###################################################### 5.
# global_sum = 0
# breaking = False
#
#
# def summerizer(inp):
#     array = inp.split(' ')
#     array_len = len(array)
#     i = 0
#     local_sum = 0
#     brek = False
#     while i < array_len:
#         if array[i] == 'END':
#             brek = True
#             break
#         elif array[i] == '':
#             array.pop(i)
#             array_len -= 1
#         else:
#             local_sum += int(float(array[i]))
#             i += 1
#     return [local_sum, brek]
#
#
# while not breaking:
#     arr = input('numbers array: ')
#     global_sum += (summerizer(arr))[0]
#     print(global_sum)
#     breaking = (summerizer(arr))[1]
# print('cycle finished')
################################################### 6&7.
# def capitaliser(inp):
#     words = inp.split(' ')
#     fixedwords = list()
#     wamount = len(words)
#     i = 0
#     while i < wamount:
#         newword = words[i].capitalize()
#         fixedwords.append(newword)
#         i += 1
#     return fixedwords
#
#
# print(capitaliser(input('words ')))
#####################################################