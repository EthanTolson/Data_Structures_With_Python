class CircleQueue():
    def __init__(self):
        # Store the length so that we can access it in O(1) time
        self.length = 0
        # Dynamic array that holds the data
        self.queue = []

    def enqueue(self, data):
        # Add to the end of the queue
        self.queue.append(data)
        # Adjust the length
        self.length += 1

    def dequeue(self):
        # if there is nothing in the queue then we cant return 
        # anything
        if self.length > 0:
            # Adjust the length
            self.length -= 1
            """
            When we dequeue instead of removing from the list 
            we want to shift the first element to the end
            thats whats makes it a circular queue
            """
            data = self.queue.pop(0)
            # Use the enqueue function to add the value 
            # back to the end of the queue
            self.enqueue(data)
            """
            End of Example
            """
            # The first item in the queue gets returned
            return data

    def size(self):
        # Returns the size of the queue
        return self.length

    def empty(self):
        # Returns true if the queue is empty
        return self.length <= 0

    # The __str__ function allows us to print our queue
    def __str__(self):
        return str(self.queue)

# Create our queue object
circularqueue = CircleQueue()

# Add 1-5 to our queue
circularqueue.enqueue(1)
circularqueue.enqueue(2)
circularqueue.enqueue(3)
circularqueue.enqueue(4)
circularqueue.enqueue(5)
# Check to make sure everything was added correctly
print(circularqueue)

# When we dequeue it should place 1 at the end of our queue
circularqueue.dequeue()
print(circularqueue)