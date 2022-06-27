class BinaryTree():
    def __init__(self):
        self.root = None
        self.length = 0

    def findoccurences(self, data, node = None):
        """
        Your code Here
        You will use recursion to solve this problem
        Make sure all of your base cases are covered
        """
        
        """End of Code"""
        pass

    def addtotree(self, data, node = None):
        """
        This function inserts a node into our Binary search tree
        It uses recursion to find the correct spot to place the node
        Each function call creates a smaller problem by moving down the tree until there are no more nodes
        """
        # This if statement will be entered only when the function is first called
        if node == None:
            # Base Case
            if self.root == None:
                # if there is no root then the node becomes the root
                newnode = BinaryTree.Node(data)
                self.root = newnode
                self.length += 1
                return
            # Recursive Call
            else:
                # If there is a root then start there to check where to add the node
                self.addtotree(data, self.root)

        # This tree will place items to the right if they are greater than or equal to the current node
        elif data >= node.data:
            # Base Case
            if node.right == None:
                newnode = BinaryTree.Node(data)
                node.right = newnode
                self.length += 1
                return
            # Recursive Call
            else:
                self.addtotree(data, node.right)
        # This tree will place items to the left if they are less than the current node
        elif data < node.data:
            # Base Case
            if node.left == None:
                newnode = BinaryTree.Node(data)
                node.left = newnode
                self.length += 1
                return
            # Recursive Call
            else:
                self.addtotree(data, node.left)

    def contains(self, data, node = None):
        """
        This function checks if some value is in our tree
        It recursively traverses the tree until it find the value or hits a leaf
        """
        # This if statement will be entered only when the function is first called
        if node == None:
            # Base Case
            if self.root == None:
                # if there is no root then return false
                return False
            # Recursive Call
            else:
                # If there is a root then start there
                return self.contains(data, self.root)
        # Base case
        elif data == node.data:
            return True
        # This tree will place items to the right if they are greater than the current node 
        # so we should check the right node when the data is greater than the current node
        elif data > node.data:
            # Base Case
            if node.right == None:
                return False
            # Recursive Call
            else:
                return self.contains(data, node.right)
        # This tree will place items to the left if they are less than the current node
        # so we should check the left node when the data is less than the current node
        elif data < node.data:
            # Base Case
            if node.left == None:
                return False
            # Recursive Call
            else:
                return self.contains(data, node.left)
        """End of Example"""

    def getHeight(self, node = None):
        """
        This function returns the height of the tree
        This function uses recursion to find the branch with the longest height and returns it
        The problem gets smaller by traversing the tree until there are no more node to traverse
        """
        if node == None:
            # Base Case
            if self.root == None:
                return 0
            # Recursive Call
            return self.getHeight(self.root)

        # Base Case
        elif node.left == None and node.right == None:
            return 0

        # Recursive Call
        if node.left == None:
            return 1 + self.getHeight(node.right)

        # Recursive Call
        elif node.right == None:
            return 1 + self.getHeight(node.left)
        
        # Recursive Call
        else:
            if self.getHeight(node.right) >= self.getHeight(node.left):
                return 1 + self.getHeight(node.right)
            else:
                return 1 + self.getHeight(node.left)

    class Node():
        # Simple Node Class
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

"""
Tests

Should Print
"6
2
0"
"""

tree = BinaryTree()
tree.addtotree(3)
tree.addtotree(4)
tree.addtotree(2)
tree.addtotree(2)
tree.addtotree(1)
tree.addtotree(2)
tree.addtotree(3)
tree.addtotree(4)
tree.addtotree(2)
tree.addtotree(2)
tree.addtotree(1)
tree.addtotree(2)

print(tree.findoccurences(2))
print(tree.findoccurences(4))
print(tree.findoccurences(9))