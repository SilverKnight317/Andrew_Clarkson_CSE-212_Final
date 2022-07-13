'''
Solveable Problem
03_Tree
'''

class Tree:
    class Node:
        def __init__(self, data):
            # When the Node is created it makes sure the pointers to both left and right areas are empty.
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # When the Tree is first initialized it sets the root as empty so the first point of data will go into 
        self.root = None

    def insert(self, data):
        # if the root node is empty then the data gets set to that root node
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # if our data is smaller than the current node's data then we'll go to the left node
        if data < node.data:
            # if the current node is empty then we'll save the data here, if not we'll move again
            if node.left is None:
                node.left = Tree.Node(data)
            else:
                self._insert(data, node.left)
        # if our data is larger than the current node's data then we'll go to the right node
        else:
            if node.right is None:
                node.right = Tree.Node(data)
            else:
                self._insert(data, node.right)
 
    def __iter__(self):
        yield from self.move_forward(self.root)

    def move_forward(self, node):
        if node is not None:
            yield from self.move_forward(node.left)
            yield node.data
            yield from self.move_forward(node.right)




tree = Tree()
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(9)
for x in tree:
    print(x)