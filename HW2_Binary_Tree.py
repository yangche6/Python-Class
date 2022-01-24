class BinaryTree: #creating a class that contains 1 Node value and 2 empty children
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def insert(root, key): #comparing for values and Inserting them into boxes
    if not root:
        return BinaryTree(key) #If theres no root, new value becomes the root
    if key > root.value:
        root.right = insert(root.right, key) #If new value greater than root, insert it into the right child box
    elif key < root.value:
        root.left = insert(root.left, key) ##If new value less than root, insert it into the left child box
    return root

def insert_values(root, values): # Run each sigle value through the "insert" function that defined before
    for value in values:
        root = insert(root, value)
    return root

def printTree(root, space=0, LEVEL_SPACE = 5):  #Tree printing, copied from Internet, did a rough guess, not really understand the syntax *_*
    if (root == None): return
    space += LEVEL_SPACE
    printTree(root.right, space)
    for i in range(LEVEL_SPACE, space): print(end = " ")  
    print("|" + str(root.value) + "|<")
    printTree(root.left, space)

list=[] #creating an empty list

#use for loop to convert string to a list
list=[int(numbers) for numbers in input("Please enter your numbers seprated with SPACE: ").split()]


tree = insert_values(None, list)
printTree(tree)  