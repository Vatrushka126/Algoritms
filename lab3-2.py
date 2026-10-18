stack = []
seq = input()
correct = True

for elem in seq:
    if elem == "(" or elem == "[" or elem == "{":
        stack.append(elem)
    else:
        if len(stack) == 0:
            correct = False
            break

        if stack[-1] == "(" and elem == ")" or stack[-1] == "[" and elem == "]" or stack[-1] == "{" and elem == "}":
            stack.pop()
        else:
            correct = False
            break

if len(stack) != 0:
    correct = False

if correct:
    print("yes")
else:
    print("no")