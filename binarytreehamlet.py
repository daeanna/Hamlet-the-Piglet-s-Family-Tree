# Binary Tree Example: Hamlet the Piglet's Family Tree

"""
In the list_family method, the 'r' and 'l' stand for 'right' and 'left' respectively. 
They indicate the side of the parent node where the current node is located in the binary tree.
"""

class Node:
    def __init__(self, piglet=None):
        self.left = None
        self.right = None
        self.piglet = piglet
    
    def insert(self, new_piglet):
        """
        Inserts a new piglet into the family tree.
        """
        if new_piglet.name < self.piglet.name:
            if self.left is None:
                self.left = Node(new_piglet)
            else:
                self.left.insert(new_piglet)
        elif new_piglet.name > self.piglet.name:
            if self.right is None:
                self.right = Node(new_piglet)
            else:
                self.right.insert(new_piglet)

    def list_family(self, depth=0, side=''):
        """
        Lists the family members in a hierarchical representation.
        """
        family = ''

        # In-order traversal to list the family members
        if self.right:
            family += self.right.list_family(depth + 1, 'r')
        family += '  ' * depth + side + '-' + self.piglet.name + '\n'
        if self.left:
            family += self.left.list_family(depth + 1, 'l')

        return family

# Piglet class
class Piglet:
    def __init__(self, name):
        self.name = name
    
    def speak(self, other=None):
        if other:
            print(f"Hi, {other.name}! I'm {self.name}. Oink!")
        else:
            print(f"Oink! I'm {self.name}! Oink!")

# Create the initial family tree
hamlet = Piglet("Hamlet")
root = Node(hamlet)

# Add more piglets to the family tree
petunia = Piglet("Petunia")
babe = Piglet("Babe")
wilbur = Piglet("Wilbur")

root.insert(petunia)
root.insert(babe)
root.insert(wilbur)

# Visualize the family tree
print("Family Tree:")
print(root.list_family())


