'''
Solveable Problem
03_Tree
Storyline:
Jerry wants to build a tree to build his database of his family tree. He 
wants to make sure his Dad (Larry) and his Mom (Mary) are connected to
him, and once he's done with that he can then connect them to their 
parents.
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
        When planning on how to set the relation between father and mother
        follow this guideline:
        relation of 1: Father
        relation of 2: Mother

        At the very beginning of inserting a person into their tree, any
        number shouldn't matter, but I'd just do 0 since it's separate 
        from the others
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
        # node = self.search_name(self.root, name)
        node = self.searchy_boy(self.root, name)
        print(node.name)

    def search_name(self, node, name):
        if node.name == name:
            return node
        # Condition of going towards the father
        father = self.search_name(node.father, name)
        if father.name != None:
            return father
        # Condition of going towards the mother
        mother = self.search_name(node.mother, name)
        if mother.name != None:
            return mother
        return None

    def searchy_boy(self, node, name):
        if node.name == name:
            return node
        # father = node.father
        if node.father is not None:
            print(node.father.name)
            padre = self.searchy_boy(node.father, name)
            if padre.name is not None:
                return padre
            return None
        # mother = node.mother
        if node.mother is not None:
            print(node.mother.name)
            madre = self.searchy_boy(node.mother, name)
            if madre.name is not None:
                return madre
            return None
        return None

fam = FamilyTree()
fam.insert("Jerry") # root
fam.insert("Larry") # Dad       1
fam.insert("Mary")  # Mom       2
fam.insert("Barry") # Dad's Dad 1, 1
fam.insert("Sue")   # Dad's Mom 1, 2
fam.insert("Harry") # Mom's Dad 2, 1
fam.insert("Linda") # Mom's Mom 2, 2


fam.name_search("Sue")