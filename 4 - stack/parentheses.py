from stack import Stack

'''
Поэлементно передаем строку в стек.
Если это "(", то положим в стек. Если ")", то удалим из стека "(".
Но перед удалением проверим, не равен ли размер стека нулю. Если равен, то количество
"(" превышает количество ")" --> баланса нет.

После завершения цикла проверяем размер стека. Если он больше нуля, то количество "(" больше
количества ")"  --> баланса нет.

Если размер стека равен нулю, то количеcтва "(" и ")" равны, и каждой открывающей соответствует
закрывающая скобка. Сбалансированы.
'''

def parentheses(s):

    if len(s) == 0:
        print("Пустая строка")
        return

    stack = Stack()

    for i in range(len(s)):
        if s[i] == "(":
            stack.push(s[i])
        elif stack.size() == 0:
            print("Скобки не сбалансированы")
            return
        else:
            stack.pop()

    if stack.size() > 0:
        print("Скобки не сбалансированы")
        return


    if stack.size() == 0:
        print("Скобки сбалансированы")
        return



#stroka_balance1 = "(()())"
stroka_balance1 = "(())()"
stroka_balance2 = "(())()()"
stroka_not_balance1 = ")())("
stroka_not_balance2 = "()((()"
stroka_empty = ""
parentheses(stroka_balance1)
print("--------------")
parentheses(stroka_balance2)
print("--------------")
parentheses(stroka_not_balance1)
print("--------------")
parentheses(stroka_not_balance2)
print("--------------")
parentheses(stroka_empty)