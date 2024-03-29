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
        relation = int(input(f"In relation to {node.name}, where does {name} go? \n1. Dad/Dad's side\n2. Mom/Mom's side\n "))
        if relation == 1:
            if node.father is None:
                node.father = FamilyTree.Member(name)
            else:
                self._insert(name, node.father)
        else:
            if node.mother is None:
                node.mother = FamilyTree.Member(name)
            else:
                self._insert(name, node.mother)

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
fam.insert("Jerry") # root      these are the numbers to put in order:
fam.insert("Larry") # Dad               1
fam.insert("Mary")  # Mom               2
fam.insert("Barry") # Dad's Dad         1, 1
fam.insert("Sue")   # Dad's Mom         1, 2
fam.insert("Harry") # Mom's Dad         2, 1
fam.insert("Linda") # Mom's Mom         2, 2

fam.name_search("Larry")
fam.name_search("Mary")