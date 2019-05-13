'''
7.2. Напишите функцию, которая с помощью deque проверяет,
является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
'''

from deque import Deque

def find_polindrom(string):
    deq = Deque()

    for s in string:
        deq.addFront(s)

    while deq.size() > 1:
        if deq.removeFront() != deq.removeTail():
            return False

    return True



string = input("Введите строку: ")
string = ''.join(string.split()) #убираем пробелы и склеиваем символы
string = "".join(c for c in string if c not in ('!','.',':','?',',')) #убираем знаки препинания
string = string.lower() #приводим к нижнему регистру

if find_polindrom(string) == True:
    print("Это палиндром")
else:
    print("Это не палиндром")