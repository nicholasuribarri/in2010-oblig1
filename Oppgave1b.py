import sys
class AVL_Node:
    def __init__(v, x):
        v.left = None
        v.right = None
        v.element = x
        v.height = 0

class AVL:
    def __init__(self):
        self.s = 0
        self.root = None
        self.h = -1

    def insert(self, x):
        if not self.contains(x):
            self.root = self._insert(self.root, x)
            self.s +=1
    def _insert(self, v, x):
        # Oppretter node ved løvnode
        if not v:
            #self.s += 1
            #print(x," Lagt til size: ", self.s, ", ekte size: ", self.count_nodes(self.root))
            return AVL_Node(x)

        # Traverserer
        if x < v.element:
            v.left = self._insert(v.left, x)
        elif x > v.element:
            v.right = self._insert(v.right, x)
        

        self.set_height(v)
        return self.balance(v)

        # returnerer rot-node
        return v


    def remove(self, x):
        if self.contains(x):
            self.root = self._remove(self.root,x)
            self.s -= 1
    def _remove(self,v, x):
        if not v:
            return None 
        
        # traverserer nedover barna
        if x < v.element:
            v.left = self._remove(v.left, x)
        elif x > v.element:
            v.right = self._remove(v.right, x)
        
        #sjekker om har 1 eller 0 barn:
        elif not v.left:
            v = v.right
        elif not v.right:
            v = v.left
        # har 2 barn
        else:
            u = self.find_min(v.right)
            v.element = u.element
            v.right = self._remove(v.right, u.element)

        self.set_height(v)
        return self.balance(v)
        # Returnerer ny rotnode
        return v
    def find_min(self,v):
        if not v.left:
            return v
        return self.find_min(v.left) 
    
    def contains(self, x):
        return self._contains(self.root, x)
    def _contains(self,v,x):
        if not v:
            return False
        #print("sammenlikner ", v.element, "og",x)
        if v.element == x:
            return True
        if x < v.element:
            return self._contains(v.left,x)
        if x >= v.element:
            return self._contains(v.right,x)

    def size(self):
        return self.s
    
    def height(self, v):
        # returnerer -1 dersom v = None
        if not v:
            return -1
        # returnerer høyde n til noden
        return v.height
        
    def set_height(self, v):
        if not v:
            return
        v.h = 1 + max(self.height(v.left), self.height(v.right))
    
    def right_rotation(self, z):
        y = z.right
        t1 = y.left
        
        z.right = t1
        y.left = z

        self.set_height(z)
        self.set_height(y)

        return y
    
    def left_rotation(self,z):
        y = z.left
        t2 = y.right

        y.right = z
        z.left = t2

        self.set_height(z)
        self.set_height(y)

        return y
    
    def balance_factor(self, v):
        if not v:
            return 0
         
        bf = self.height(v.left) - self.height(v.right)
        #print(bf)
        return bf
    
    def balance(self, v):
        if self.balance_factor(v) < -1: # hvis det er fra og med -1 til og med 1, oppfyller det kravene
            # Sjekker om vi må ha en høyrerotasjon i tillegg
            if self.balance_factor(v.right) > 0:
                v.right = self.right_rotation(v.right)
            return self.left_rotate(v)
        if self.balance_factor(v) > 1:
            if self.balance_factor(v.left) < 0:
                v.left = self.left_rotation(v.left)
            return self.right_rotation(v)
        return v
        
input = sys.stdin.read().splitlines() # en liste med 1 element for hver linje
tree = AVL()
root = tree.root

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

