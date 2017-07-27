import re

def polish(expr):
    stack = []

    token_list = expr.split()

    for token in token_list:
        if isNumber(token):
            stack.append(int(token))
        elif token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())

    if len(stack) == 1:
        return stack[0]
    else:
        pass

def isNumber(str):
    return None != re.match("\d+", str)

print(21 == polish("1 2 + 3 4 + *"))
print(64 == polish("3 5 + 8 *"))
print(30 == polish("1 2 3 4 5 + * + +"))
