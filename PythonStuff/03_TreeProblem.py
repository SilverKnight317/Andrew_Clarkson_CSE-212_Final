'''
Solveable Problem
03_Tree
Storyline:
Jerry wants to build a tree to build his database of his family tree. He 
wants to make sure his Dad (Larry) and his Mom (Mary) are connected to
him, and once he's done with that he can then connect them to their 
parents.
After getting their parents connected to them, he wants to see his tree
print out what each of his parents are.
'''

class FamilyTree:
    
    class Member:

        def __init__(self, name):
            self.name = name
            self.father = None
            self.mother = None

    def __init__(self):
        self.root = None

    def insert(self, name):
        """
        After Jerry is inserted each person's relation
        will need to be defined.
        """
        if self.root is None:
            self.root = FamilyTree.Member(name)
        else:
            self._insert(name, self.root)

    def _insert(self, name, node):
        '''
        code goes here.
        Don't forget that each person's relation to their
        child needs to be added in. The solution goes 
        through each relation individually.
        '''

    def name_search(self, name):
        '''
        This is where the search algorithm "searchy_boy" will
        get started.
        '''
        node = self.searchy_boy(self.root, name)
        print(f"Father of {node.name}: " + node.father.name)
        print(f"Mother of {node.name}: " + node.mother.name)

    def searchy_boy(self, node, name):
        '''
        function using recursion to find the specific name through the whole
        tree.
        '''
        if node.name == name:
            return node
        if node.father is not None:
            # print(node.father.name) # Debug for making sure you can see where it'll try to head towards
            padre = self.searchy_boy(node.father, name)
            if padre is not None:
               return padre
        if node.mother is not None:
            # print(node.mother.name) # Debug for making sure you can see where it'll try to head towards
            madre = self.searchy_boy(node.mother, name)
            if madre is not None:
                return madre
        return None

fam = FamilyTree()
fam.insert("Jerry") # root
fam.insert("Larry") # Dad
fam.insert("Mary")  # Mom
fam.insert("Barry") # Dad's Dad
fam.insert("Sue")   # Dad's Mom
fam.insert("Harry") # Mom's Dad
fam.insert("Linda") # Mom's Mom

fam.name_search("Larry")
fam.name_search("Mary")