class PostOrder:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

def main():

    root = PostOrder(1)
    root.left = PostOrder(2)
    root.right = PostOrder(3)
    root.left.left = PostOrder(4)
    root.left.right = PostOrder(5)

    root.postOrder(root)

main()