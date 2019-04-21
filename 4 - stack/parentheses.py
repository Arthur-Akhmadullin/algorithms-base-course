from stack import Stack


def parentheses(s):

    stack = Stack()

    if s[0] == ")" or s[len(s)-1] == "(" or len(s) % 2 != 0:
        print("Скобки не сбалансированы")
        return

    for i in range(len(s)):
        if s[i] == "(":
            stack.push("open")
        else:
            stack.pop()

        if stack.size() == 0 and i != (len(s) - 1) and (i+1) == ")":
            print("Скобки не сбалансированы")
            return

        if stack.size() == 0:
            print("Скобки сбалансированы")
            return


stroka_balance1 = "()()()"
stroka_balance2 = "(())()()"
stroka_not_balance1 = "())("
stroka_not_balance2 = "()(()"
parentheses(stroka_balance1)
print("--------------")
parentheses(stroka_not_balance1)
print("--------------")
parentheses(stroka_balance2)
print("--------------")
parentheses(stroka_not_balance2)