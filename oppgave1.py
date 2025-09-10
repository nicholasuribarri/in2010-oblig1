class BST:
    def __init__(self):
        self.root = None
        self._size = 0


    def contains(self, x):
        if self.root:
            return self.root.contains(x)
        else:
            return False
      
    def size(self):
        return self._size
    
    def insert(self, x):
        #Hvis treet ikke er tomt, bruk insert fra Node- klassen, ellers bare lag en node i root
        if self.root:
            if not self.contains(x):
                self.root.insert(x)
                self._size += 1
        else:
            self.root = BST.Node(x)
            self._size += 1
        
    
    def remove(self, x):
        if self.root and self.contains(x):
            self.root = self.root.remove(x)
            self._size -= 1
        

    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


        def contains(self, x):

            if self.value == x:
                return True
            
            if self.value > x:
                if self.left:
                    return self.left.contains(x)
                else: 
                    return False
            else:
                if self.right:
                    return self.right.contains(x)
            return False
                
            
            
        def insert(self, x):
            if self.value == x:
                return
            
            if self.value > x:
                if self.left is None:
                    self.left = BST.Node(x)
                else:
                    return self.left.insert(x)
                
            if self.value < x:
                if self.right is None:
                    self.right = BST.Node(x)
                else:
                    return self.right.insert(x)
                
                
        def remove(self, x):

            #Søk gjennom treet til vi har en Node med riktig verdi

            if x is None:
                return None
            
            if x < self.value:
                if self.left:
                    self.left = self.left.remove(x)
            elif x > self.value:
                if self.right:
                    self.right = self.right.remove(x)
            else:
            #Funnet riktig Node

            #Case 1: Ingen barn
                #if not self.left and not self.right:
                    # return None

            #Case 2: Ett barn
                if not self.left:
                    return self.right
                elif not self.right:
                    return self.left
            #Case 3: To barn
                else:
                    smallest_child_right = self.right.find_min()
                    self.value = smallest_child_right.value
                    self.right = self.right.remove(smallest_child_right.value)
            
            return self


        def find_min(self):
            if self.left:
                return self.left.find_min()
            else:
                return self
            




t = BST()

stdin = open("input_100000.txt", "r")
stdout = open("output_100000.txt", "w")

first_line = stdin.readline()

for i in range(int(first_line)):
    line = stdin.readline()

    if line.startswith("insert"):
        parts = line.split()
        t.insert(parts[1])
        #print("insert", parts[1])
    elif line.startswith("size"):
        parts = line.split()
        stdout.write(str(t.size())+"\n")
        #print("size", t.size())
    elif line.startswith("contains"):
        parts = line.split()
        stdout.write(str(t.contains(parts[1]))+"\n")
        #print("contains", parts[1], t.contains(parts[1]))
    elif line.startswith("remove"):
        parts = line.split()
        t.remove(parts[1])
        #print("remove", parts[1])
 
stdin.close()
stdout.close()
    