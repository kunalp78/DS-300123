class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.HEAD = None

if __name__ == '__main__':

    llist = LinkedList()

    llist.HEAD = Node("Alina")
    print(llist.HEAD.data)
    llist.HEAD.next = Node("Aakash")
    print(llist.HEAD.next.data)
    llist.HEAD.next.next = Node("Neha")