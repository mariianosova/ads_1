from math import factorial

data = input().split()

stack = []

for elem in data:
    if elem.isdigit():
        stack.append(int(elem))
    elif elem == "+":
        stack.append(stack.pop() + stack.pop())
    elif elem == "*":
        stack.append(stack.pop() * stack.pop())
    elif elem == "-":
        second = stack.pop()
        first = stack.pop()
        stack.append(first - second)
    elif elem == "/":
        second = stack.pop()
        first = stack.pop()
        stack.append(first // second)
    elif elem == "~":
        stack.append(-stack.pop())
    elif elem == "!":
        stack.append(factorial(stack.pop()))
    elif elem == "#":
        elem = stack.pop()
        stack.append(elem)
        stack.append(elem)
    elif elem == "@":
        third = stack.pop()
        second = stack.pop()
        first = stack.pop()
        stack += [second, third, first]
    
print(stack[0])