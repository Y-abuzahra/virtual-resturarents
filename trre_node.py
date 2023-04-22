class TreeNode():
    def __init__(self, value):
        self.value = value

        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    def traverse(self):
        if self == None:
            return None
        
        print(self.value)
        for child in self.children:
            child.traverse()

