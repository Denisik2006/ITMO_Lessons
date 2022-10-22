# def do_nothing():
#     pass
#
#
# do_nothing()
#
#
# def returns_True():
#     return True
#
#
# def check_triangle(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     if a + b < c:
#         return False
#     if b + c < a:
#         return False
#     if a + c < b:
#         return False
#     return True
#
#
# check_triangle(1, 2, 2)
# check_triangle(1, 2, 3)
#
#
# def umnog(a, b=2):
#     c = a * b
#     return c
#
#
# print(umnog(1))


# def not_buggy(value, array=None):
#     if array is None:
#         array = []
#         array.append(value)
#     return array
#
#
# print(not_buggy(1))
# print(not_buggy(2))

#
# def un_param(*args):
#     print(args)
#
#
# print(un_param(1, 1, 1, 1, 1))
# print(un_param(6, 6, 6))


# - напишите функцию, которая принмает на вход произвольное количество аргументов и выдает сумму этих аргументов
# - сделaйте коммит
# - допишите функцию так, чтобы она проверяла, что вы передали только числа. Если попадаются не числа, то напечатайте сообщение об ошибке
# - сделайте коммит
#
#
# - создайте новую ветку
# - переключитесь на нее
# - напишите функцию, которая определяет, является ли строка палиндромом
#
#
# - создайте новую ветку
# - переключитесь на нее
# - напишите функцию, которая удаляет из строки лишние пробелы
def summa(*args):
    a = 0
    for i in args:
        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
            continue
        else:
            a += 1
    if a != 0:
        print('Wrong parametrs')
    else:
        print(sum(args))


summa(1, 2, 3, 4, 'a', 6, 7)


def palindrom(a):
    if str(a) == "".join(reversed(a)):
        print("Palindrome")
    else:
        print("Not Palindrome")


a = input('Введите слово')
palindrom(a)


def space(a):
    b = a.replace(' ', '')
    print(b)


a = str(input('Введите словосочетание'))
space(a)
