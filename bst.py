class BinarySearchTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    def search(self, root, value):
        if root is None:
            return
        
        if root.val == value:
            print("Value found")
            return
        
        self.search(root.left, value)
        self.search(root.right, value)
        

def main():

    root = BinarySearchTree(1)
    root.left = BinarySearchTree(2)
    root.right = BinarySearchTree(3)
    root.left.left = BinarySearchTree(4)
    root.left.right = BinarySearchTree(5)

    root.search(root, 9)

main()