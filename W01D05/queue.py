MAX = 5
items = [0]*5
front = rear = -1

def enqueue(val):
    """
    to enqueue the item in stack
    Rear value will increase till MAX - 1
    """
    global front
    global rear
    if rear == MAX - 1:
        print("Queue is full")
    else:
        if front == -1:
            front = 0
        rear += 1
        items[rear] = val
        print(front, rear)

def dequeue():
    """
    to dequeue the item in stack while reducing the Front
    value till -1
    """
    global front
    global rear
    if front == -1:
        print("Queue is Empty")
    else:
        print(f"Deleted --> {items[front]}")
        front += 1
        if front > rear:
            front = rear = -1
        print(front , rear)


enqueue("Alina")
enqueue("Nooh")
enqueue("jaihind")
enqueue("Aakash")
enqueue("Bharathi")

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()