class preOrder:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    def preOrder(self, root):

        if root is None:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

def main():

    root = preOrder(1)
    root.left = preOrder(2)
    root.right = preOrder(3)
    root.left.left = preOrder(4)
    root.left.right = preOrder(5)

    root.preOrder(root)

main()

        