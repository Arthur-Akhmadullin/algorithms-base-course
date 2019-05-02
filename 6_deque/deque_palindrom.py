'''
7.2. Напишите функцию, которая с помощью deque проверяет,
является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
'''

from deque import Deque

string = input("Введите строку: ")
string = ''.join(string.split()) #убираем пробелы и склеиваем символы
string = "".join(c for c in string if c not in ('!','.',':','?',',')) #убираем знаки препинания
string = string.lower() #приводим к нижнему регистру

def find_polindrom(string):
    deq = Deque()
    for i in range(len(string)):
        deq.addFront(string[i])
        deq.addTail(string[len(string) - 1 - i])
        if deq.removeFront() != deq.removeTail():
            print("Это не палиндром")
            return
        i += 1
    print("Это палиндром")
    return

find_polindrom(string)