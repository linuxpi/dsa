class Node:
    value = None
    children = None

    def __init__(self, value, children = None):
        if value is None:
            raise Exception("value cannot be null")
        self.value = value
        self.children = children or []

class Solution:
    stackFlip = False
    stackA = []
    stackB = []

    def traverse(self, root):
        self.appendToStack(root)
        while self.stackA or self.stackB: 
            self.flipStack()
            [self.processNode(child) for child in self.getNextNode()]

    def processNode(self, node):
        print(node.value)
        children = self.getAllChildren(node)
        if self.stackFlip:
            children.reverse()
        [self.appendToStack(child) for child in self.getAllChildren(node)]

    def getAllChildren(self, node):
        return node.children

    def flipStack(self):
        self.stackFlip = not self.stackFlip

    def appendToStack(self, node):
        if self.stackFlip:
            self.stackB.append(node)
        else:
            self.stackA.append(node)
    
    def getNextNode(self):
        stack = self.stackA if self.stackFlip else self.stackB
        while stack:
            yield stack.pop()

d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

b = Node("b", [d, e])
c = Node("c", [f, g])
a = Node("a", [b,c])

Solution().traverse(a)
