# Stack implementation using list

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop operation
if len(stack) == 0:
    print("Stack Underflow")
else:
    removed = stack.pop()
    print("Popped element:", removed)

print("Stack after pop:", stack)