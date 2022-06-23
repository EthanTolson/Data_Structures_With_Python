class UniqueQueue():
    def __init__(self):
        # Store the length so that we can access it in O(1) time
        self.length = 0
        # Dynamic array that holds the data
        self.queue = []

    def enqueue(self, data):
        """
        Code Goes Here
        Dont forget about the length
        """
        
        """
        End of problem
        """
        pass

    def dequeue(self):
        # if there is nothing in the queue then we cant return 
        # anything
        if self.length > 0:
            # Adjust the length
            self.length -= 1
            # The first item in the queue gets returned
            return self.queue.pop(0)

    def size(self):
        # Returns the size of the queue
        return self.length

    def empty(self):
        # Returns true if the queue is empty
        return self.length <= 0

    # The __str__ function allows us to print our queue
    def __str__(self):
        return str(self.queue)

"""
Test

Expected Output True
"""
# Create queue
uniqqueue = UniqueQueue()

# Try to add mulitple of certain values
uniqqueue.enqueue(1)
uniqqueue.enqueue(2)
uniqqueue.enqueue(1)
uniqqueue.enqueue(3)
uniqqueue.enqueue(1)
uniqqueue.enqueue(4)
uniqqueue.enqueue(5)
uniqqueue.enqueue(5)

print("[1, 2, 3, 4, 5]" == str(uniqqueue))