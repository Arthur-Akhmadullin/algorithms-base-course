from stack import Stack

# Можно попросить ввести запись с клавиатуры
# str = input("Постфиксная запись: ")
# но я ее передам сразу:
str = "8 2 + 5 * 9 + ="

def postfix(str):
    stack1 = Stack()
    stack2 = Stack()
    string = ''.join(reversed(str.split()))


    for i in range(len(string)):
        stack1.push(string[i])

    while stack1.size() > 0:
        elem = stack1.pop()

        if elem == "=":
            return stack2.peek()
        elif elem not in "+-*/":
            stack2.push(int(elem))
        else:
            b = stack2.pop()
            a = stack2.pop()
            if elem == "+":
                result = a + b
            elif elem == "-":
                result = a - b
            elif elem == "*":
                result = a * b
            else:
                result = a / b
            stack2.push(result)

print("Результат: ")
print(postfix(str))