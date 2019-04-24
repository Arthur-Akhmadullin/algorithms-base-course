from stack import Stack

'''
Баланс скобок отслеживается в переменной balance.
Если из стека вытащили закрывающую скобку, то увеличим balance на единицу.
Если открывающую, то, наоборот, уменьшим на единицу.
Если в процессе освобождения стека balance стала меньше нуля, то скобки заведомо
не сбалансированы.
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



stroka_balance1 = "(()())"
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