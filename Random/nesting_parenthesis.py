def nesting_parenthesis(tags: str) -> bool:
    if not tags:
        return True
    stack = []
    for i in tags:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif i == '}':
            if stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif i == ']':
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        return len(stack) == 0

print(nesting_parenthesis(""))
print(nesting_parenthesis("()"))
print(nesting_parenthesis("())"))
print(nesting_parenthesis("(ae()2)"))
