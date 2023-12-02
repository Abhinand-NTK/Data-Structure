# stack = []

# stack.append(9)
# stack.append(4)
# stack.append(6)

# print(stack)

# stack.pop()
# stack.pop()
# print(stack)


from collections import deque

stack = deque()

stack.append(4)
stack.append(6)
stack.append(46)

print(stack)

stack.pop()
stack.pop()

print(stack)