# Linked Lists
## Overview
[Arrays](https://www.geeksforgeeks.org/introduction-to-arrays/) are very useful in computer science but they have some weaknesses. 

The main weakness is the need for contiguous memory. 

In this image each box represents a memory location. The black dots represent memory locations that are currently in use.
The red line represents an array of size 3. Notice how the array occupies memory spaces in order.

![Array In Memory](resources/computermemoryarray.png)

What happens if we do not have enough memory spaces in order to create our array? 

In this image we see that most memory spaces are already used (filled with black dots). Because arrays use contiguous memory if we tried to create one it would either rewrite data or not be created.

![Computer Memory](resources/computermemorynoarray.png)

**Linked Lists** are similar to arrays in that they store a list of similar objects, however they do not require contiguous memeory to be implemented. A single linked list (shown below) uses nodes that store the data and the memory address of the next element in the list.

![Single Linked List](resources/singlelinkedlistfinal.png)

The arrows in the image shows how each node points to the next.

**This means that the memory that a linked list uses does not have to be contiguous.**

In this image we see a linked list with three nodes being stored in memory. Black dots represent memeory being used. Red dots represent a node in our linked list.
![Linked List in Memory](resources/computermemorylinkedlist.png)

Now we can store our data without needing a lot of extra memory!
## Doubly Linked Lists
Single Linked Lists are amazing but they have some problems when compared to arrays. The first problem that you may have recognized is that arrays are very fast at retrieving values. Because the memory is contiguous you can take the beginning address and add

![Doubly Linked List](resources/doublylinkedlistfinal.png)
## Performance
Linked lists 
## Common Uses
### Queues Using Linked Lists
## Linked Lists in Python
## Example of Using a Linked List in Python
## Try It Yourself