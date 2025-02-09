class InOrder:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)

def main():

    root = InOrder(1)
    root.left = InOrder(2)
    root.right = InOrder(3)
    root.left.left = InOrder(4)
    root.left.right = InOrder(5)

    root.inOrder(root)

main()

        