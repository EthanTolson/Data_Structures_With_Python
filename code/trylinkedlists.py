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

def combineLinkedLists(l1, l2):
    """Your code here"""

    """End of problem"""
    pass

"""
Test

Should Print "[1,2,3,2,1]
[a]
[1,2,3,2,1,a]
"""
# create the linked list
linked_list1 = DoublyLinkedList()
# insert our data into the linked list
linked_list1.inserthead(3)
linked_list1.inserthead(2)
linked_list1.inserthead(1)
linked_list1.inserttail(2)
linked_list1.inserttail(1)


print(linked_list1)

# create new linked list with only one node
linked_list2 = DoublyLinkedList()

linked_list2.inserthead("a")

print(linked_list2)

linked_list3 = combineLinkedLists(linked_list1, linked_list2)

print(linked_list3)