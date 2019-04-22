from stack import Stack

'''
Баланс скобок отслеживается в переменной balance.
Если из стека вытащили закрывающую скобку, то увеличим balance на единицу.
Если открывающую, то, наоборот, уменьшим на единицу.
Если в процессе освобождения стека balance стала меньше нуля, то скобки заведомо
не сбалансированы.
'''
def parentheses(s):

    stack = Stack()
    balance = 0

    for i in range(len(s)):
        stack.push(s[i])

    if stack.peek() == "(" or stack.size() % 2 != 0:
        print("Скобки не сбалансированы")
        return

    while stack.size() > 0:
        if stack.pop() == ")":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            print("Скобки не сбалансированы")
            return

    if balance == 0:
        print("Скобки сбалансированы")
        return



stroka_balance1 = "(()())"
stroka_balance2 = "(())()()"
stroka_not_balance1 = "())("
stroka_not_balance2 = "()((()"
parentheses(stroka_balance1)
print("--------------")
parentheses(stroka_balance2)
print("--------------")
parentheses(stroka_not_balance1)
print("--------------")
parentheses(stroka_not_balance2)