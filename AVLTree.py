class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None


    def right_rotate(self, node):
        return
    
    def left_rotate(self, node):
        return
    
    def set_height(self, node):
        node.height = max(node.left.get_height(), node.right.get_height()) + 1

    
    def get_height(self, node):
            if node is None:
                return 0
            else:
                return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        else:
            return self.get_height(node.left) - self.get_height(node.right)
        
    def balance(self, node):
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        return node
    

        
        

