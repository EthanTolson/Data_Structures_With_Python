class DoublyLinkedList():
    # Create an empty linked list with a length, head, and tail attribute
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def inserthead(self, data):
        # Create a new node
        node = DoublyLinkedList.Node(data)

        # If there is nothing in the list then the new node 
        # is both the head and tail
        if self.head == None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        # set the previous of the current head to the new head
        self.head.previous = node
        # set the next of the new head to the previous head
        node.next = self.head
        # set the head to the new node
        self.head = node
        # add to the length
        self.length += 1

    def inserttail(self, data):
        # Create a new node
        node = DoublyLinkedList.Node(data)

        # If there is nothing in the list then the new node 
        # is both the head and tail
        if self.tail == None:
            self.tail = node
            self.head = node
            self.length += 1
            return

        # set the next of the old tail to the new node
        self.tail.next = node
        # set the previous of the node to the old tail
        node.previous = self.tail
        # set the tail to the new node
        self.tail = node
        # add to the length
        self.length += 1

    def removehead(self):
        """
        Your code here
        dont forget about length
        """

        """
        End of code
        """
        pass

    def removetail(self):
        """
        Your code here
        Dont forget about length
        """
        
        """
        End of code
        """
        pass

    def __str__(self):
        """Function returns our list as a string"""
        node = self.head
        llist_as_string = "["
        for i in range(self.length):
            if i < self.length - 1:
                llist_as_string = llist_as_string + str(node.data) + ", "
            else:
                llist_as_string = llist_as_string + str(node.data)
            node = node.next
        llist_as_string = llist_as_string + "]"
        return llist_as_string

    class Node():
        # create a new node that contains some data and information about its neighbors in the list
        def __init__(self, data):
            self.next = None
            self.previous = None
            self.data = data

"""
Test

Should Print "[2, 3, 2]"
and []
"""
# create the linked list
linked_list = DoublyLinkedList()
# insert our data into the linked list
linked_list.inserthead(3)
linked_list.inserthead(2)
linked_list.inserthead(1)
linked_list.inserttail(2)
linked_list.inserttail(1)

# Test out your answer
linked_list.removehead()
linked_list.removetail()

print(linked_list)

# create new linked list with only one node
linked_list = DoublyLinkedList()

linked_list.inserthead(1)
linked_list.removetail()
linked_list.removehead()

print(linked_list)