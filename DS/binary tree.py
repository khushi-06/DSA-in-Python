# create a class tree 
# create node


#  crreating a binary tree:
class node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

# cretating a full tree
class tree ():
    def create_node(self,data): 
        # create a node and then add data and return the value 
        return node(data)  

    def insert (self,node,data):
        if node is node:
            self.create_node(data) 
        if data<node.data:
            node.left=self.insert(node.left,data)  
  



root=node(3)
root.left=node(2)
root.right=node(4)
root.left.left=node(5)
root.left=node(6)

  

# tree travesing:
# # Python program to for tree traversals
  
# # A class that represents an individual node in a
# # Binary Tree
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
  
  
# # A function to do inorder tree traversal
# def printInorder(root):
  
#     if root:
  
#         # First recur on left child
#         printInorder(root.left)
  
#         # then print the data of node
#         print(root.val),
  
#         # now recur on right child
#         printInorder(root.right)
  
  
# # A function to do postorder tree traversal
# def printPostorder(root):
  
#     if root:
  
#         # First recur on left child
#         printPostorder(root.left)
  
#         # the recur on right child
#         printPostorder(root.right)
  
#         # now print the data of node
#         print(root.val),
  
  
# # A function to do preorder tree traversal
# def printPreorder(root):
  
#     if root:
  
#         # First print the data of node
#         print(root.val),
  
#         # Then recur on left child
#         printPreorder(root.left)
  
#         # Finally recur on right child
#         printPreorder(root.right)
  
  
# # Driver code
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print("Preorder traversal of binary tree is")
# printPreorder(root)
  
# print("\nInorder traversal of binary tree is")
# printInorder(root)
  
# print("\nPostorder traversal of binary tree is")
# printPostorder(root)
