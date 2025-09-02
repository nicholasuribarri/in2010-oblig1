
class Settt:
    root = Node(null)
    size = 0

    def __init__(self):
        self.root = root
        self.size = size


    def contains(self, x):
        return root.contains(x)
    
    def insert(self, x):
        return root.insert(x)
    

    
    class Node:
        value = null
        left, right = null

        def __init__(self, x):
            self.value = value
            self.left = left
            self.right = right


        def contains(self, x):

            if value == null:
                return False
            
            if value == x:
                return True
            
            if self.value > x:
                return this.left.contains(x)
            else:
                return this.right.contains(x)
            
        def insert(self, x):
            if this.value == x:
                return
            
            if this.value == null:
                this.value = x
                return
            
            if this.value > x:
                if this.left == null:
                    this.left = Node(x)
                else:
                    return this.left.insert(x)
                
            if this.value < x:
                if this.right == null:
                    this.right = Node(x)
                else:
                    return this.right.insert(x)
        
