class Set:
    def __init__(self):
        self.root = Node(None)
        self.size = 0


    def contains(self, x):
        return self.root.contains(x)
    
    def insert(self, x):
        return self.root.insert(x)
    
    class Node:
        def __init__(self, x):
            self.value = x
            self.left = None
            self.right = None


        def contains(self, x):

            if self.value == None:
                return False
            
            if self.value == x:
                return True
            
            if self.value > x:
                return self.left.contains(x)
            else:
                return self.right.contains(x)
            
        def insert(self, x):
            if self.value == x:
                return
            
            if self.value == None:
                self.value = x
                return
            
            if self.value > x:
                if self.left == None:
                    self.left = self(x)
                else:
                    return self.left.insert(x)
                
            if self.value < x:
                if self.right == None:
                    self.right = Node(x)
                else:
                    return self.right.insert(x)
        
