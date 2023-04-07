class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.HEAD = None
    
    def append(self, data):
        '''
        adding the new node at the end of 
        the linked list
        '''
        new_node = Node(data)
        # if the linked list is empty
        # we will connect new node to the HEAD
        if self.HEAD is None:
            self.HEAD = new_node
            return

        temp = self.HEAD
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def appendB(self, data):
        '''
        adding the new node at the begening
        of the linked list
        '''
        new_node = Node(data)
        new_node.next = self.HEAD
        self.HEAD = new_node

    def deleteB(self):
        """
        delete the new node from the Begening
        of the linked list
        """
        temp = self.HEAD
        self.HEAD = self.HEAD.next
        print(f"{temp.data} is deleted")
    
    def deleteL(self):
        """
        Delete the element from the end of the
        Linked list
        """
        temp = self.HEAD
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        print(f"{temp.data} node is deleted") 

    def printList(self):
        temp = self.HEAD
        print("HEAD -->", end = "")
        while temp:
            print(f"{temp.data} -->", end = "")
            temp = temp.next
        print("None")
if __name__ == '__main__':

    llist = LinkedList()
    llist.append("Bharathi")
    llist.append("Sayan")
    llist.append("Akash")

    llist.printList()

    llist.append("Priyanshu")
    llist.printList()

    llist.deleteB()
    llist.printList()

    llist.deleteL()
    llist.printList()