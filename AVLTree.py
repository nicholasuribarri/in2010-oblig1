import sys

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size
    
    
    def contains(self, node, x):

        if not node:
            return False

        if node.value == x:
            return True
        
        if node.value > x:
            return self.contains(node.left, x)
        elif node.value < x:
            return self.contains(node.right, x)
        
        return False
        

    def right_rotate(self, node):
        y = node.left
        t1 = y.right

        y.right = node
        node.left = t1

        self.set_height(node)
        self.set_height(y)

        return y 

    
    def left_rotate(self, node):
        y = node.right
        t1 = y.left

        y.left = node
        node.right = t1

        self.set_height(node)
        self.set_height(y)

        return y
    
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
    
    def insert(self, node, x):
        if not node:
            node = AVLNode(x)
        elif x < node.value:
            node.left = self.insert(node.left, x)
        elif x > node.value:
            node.right = self.insert(node.right, x)

        self._size += 1

        self.set_height(node)
        return self.balance(node)
    
    def find_min(self):
            if self.left:
                return self.left.find_min()
            else:
                return self

    
    def remove(self, node, x):
        if not node:
            return None
        
        if x < node.value:
            node.left = self.remove(node.left, x)
        elif x > node.value:
            node.right = self.remove(node.left, x)
        elif not node.left:
            node = node.right
        elif not node.right:
            node = node.left
        else:
            u = self.find_min(node.right)
            node.value = u.value
            node.right = self.remove(node.right, u.value)

        self._size -= 1

        self.set_height(node)
        return self.balance(node)


    

        
    

        
        



input = sys.stdin.read().splitlines() # en liste med 1 element for hver linje
tree = AVLTree()

for i in range(int(input[0])+1):

    if i == 0:
        continue
    commands = input[i].split(" ")
    c = commands[0]
    try:
        n = commands[1]
    except:
        print(tree.size())
    if c == "contains":
        if tree.contains(n):
            print("true")
        else:
            print("false")
    elif c == "insert":
        tree.insert(n)
    elif c == "remove":
        tree.remove(n)