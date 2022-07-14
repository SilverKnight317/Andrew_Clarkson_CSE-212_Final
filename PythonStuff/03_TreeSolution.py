'''
Solveable Problem
03_Tree
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
        if self.root is None:
            self.root = FamilyTree.Member(name)
        else:
            self._insert(name, self.root)

    def _insert(self, name, node):
        relation = int(input("What is {}'s relation to {}? \n1. Dad\n2. Mom\n".format(name, self.root.name)))
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

    def __iter__(self):
        
        yield from self.move_forward(self.root)

    def move_forward(self, node):
        if node is not None:
            yield from self.move_forward(node.father.name)
            yield node.name
            yield from self.move_forward(node.mother.name)


fam = FamilyTree()
fam.insert("Jerry")
fam.insert("Larry")
fam.insert("Mary")

for name in fam:
    print(name)