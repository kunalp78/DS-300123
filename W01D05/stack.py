top = -1
MAX = 3
items = [0] * MAX
count = -1

def push(data):
    global count
    global top
    #check if stack is full?
    if top == MAX -1:
        print("Stack is full!!")
    else:
        top += 1
        items[top] = data
    count += 1

def pop():
    global top
    global count
    # check if stack is empty
    if top == -1:
        print("Stack is Empty!!")
    else:
        print(f"item Popped!! {items[top]}")
        top -= 1
    count -= 1

def peek():
    return items[top]

def isEmpty():
    if top == -1:
        return 1
    else:
        return 0

def isFull():
    if top == MAX - 1:
        return 1
    else:
        return 0

def printStack():
    print("Stack")
    for i in range(0, count+1):
        print(items[i])

print(isEmpty())
push("Nooh")
push("Savita")
push("jaihind")
printStack()
# pop()
# printStack()
print(isFull())

push("Uday")
pop()
pop()
pop()
pop()