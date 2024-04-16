# Hamlet the Piglet's Family Tree

This Python code illustrates a binary tree example representing the family tree of Hamlet the Piglet. The family tree consists of nodes representing piglets, with each piglet having a left and right child node.

# Implementation Details

# `Node` Class
- The `Node` class represents a node in the binary tree.
- Each node contains references to its left and right child nodes and a `Piglet` object.
- The `insert` method inserts a new piglet into the family tree in the appropriate position based on the piglet's name.
- The `list_family` method lists the family members in a hierarchical representation using in-order traversal.

# `Piglet` Class
- The `Piglet` class represents a piglet in the family tree.
- Each piglet has a name and can speak to another piglet.

# Usage

1. Create a `Piglet` object for the root of the family tree.
2. Initialize a `Node` object with the root `Piglet`.
3. Add more piglets to the family tree using the `insert` method.
4. Visualize the family tree using the `list_family` method.

# Example Usage
hamlet = Piglet("Hamlet")
root = Node(hamlet)

Add more piglets to the family tree
petunia = Piglet("Petunia")
babe = Piglet("Babe")
wilbur = Piglet("Wilbur")

root.insert(petunia)
root.insert(babe)
root.insert(wilbur)

Visualize the family tree
print("Family Tree:")
print(root.list_family())


# Note
In the `list_family` method, the 'r' and 'l' stand for 'right' and 'left' respectively. They indicate the side of the parent node where the current node is located in the binary tree.

Feel free to customize and enhance this README as needed!
