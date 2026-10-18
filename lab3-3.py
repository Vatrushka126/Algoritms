stack = []
seq = input().split()

for elem in seq:
    if elem == "+" or elem == "-" or elem == "*":
        b = stack.pop()
        a = stack.pop()

        if elem == "+":
            stack.append(a + b)
        elif elem == "-":
            stack.append(a - b)
        elif elem == "*":
            stack.append(a * b)
    else:
        stack.append(int(elem))

print(stack[-1])