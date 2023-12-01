# class Node:
#     def __init__(self,data):
#         self.key = data
#         self.left = None
#         self.right = None
# def insert(root,key):
#     if root is None: 
#         root = Node(key)
#     if root.key > key:
#         root.left = insert(root.left,key)
#     if root.key < key:
#         root.right = insert(root.right,key)
#     return root
# i = 0
# def inorder(root):
#     global i
#     while i == 0:
#         print("Inorde Traversing----")
#         i+=1
#     if root:
#         inorder(root.left)
#         print("-->",root.key,end=",")
#         inorder(root.right)

# def preorder(root):
#     global i
#     i = 0
#     while i == 0:
#         print("\nPreorder Traversing")
#         i+=1
#     if root:
#         print("-->",root.key,end=",")
#         inorder(root.left)
#         inorder(root.right)

# def postorder(root):
#     global i
#     i = 0
#     while i == 0:
#         print("\nPostorder Traversing")
#         i+=1
#     if root:
#         print("-->",root.key,end=",")
#         inorder(root.left)
#         inorder(root.right)
# root = None

# root = insert(root,40)
# insert(root,30)
# insert(root,1220)
# insert(root,10)

# inorder(root)
# preorder(root)
# postorder(root)


##breadth first search

# class Node:
#     def __init__(self,data):
#         self.key = data
#         self.left = None
#         self.right = None
# def insert(root,key):
#     if root is None:
#         root = Node(key)
#     if root.key > key:
#         root.left = insert(root.left,key)
#     elif root.key < key:
#         root.right = insert(root.right,key)
#     return root
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print("===>>",root.key,end=",")
#         inorder(root.right)
# def height(root):
#     if root is None:
#         return 0 
#     else:
#         ldepth = height(root.left)
#         rdepth = height(root.right)
#         if ldepth > rdepth:
#             return ldepth + 1
#         else:
#             return rdepth + 1
# def printgivenlevel(root,level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.key,end=",")
#     elif level > 1:
#         printgivenlevel(root.left,level-1) 
#         printgivenlevel(root.right,level-1) 

# def pritinglevelorder(root):
#     h = height(root)
#     for i in range(1,h+1):
#         printgivenlevel(root,i)
#         print()

# root = None

# root = insert(root,50)
# insert(root,55)
# insert(root,545)
# insert(root,255)
# insert(root,53435)
# inorder(root)
# pritinglevelorder(root)


