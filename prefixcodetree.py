class PrefixCodeTree:
    class Node:
        # Node's symbol is not None if it's a leaf
        def __init__(self):
            self.left = None
            self.right = None
            self.symbol = None
        
        def getNodeLeft(self):
            if not self.left:
                self.left = PrefixCodeTree.Node()
            return self.left
        
        def getNodeRight(self):
            if not self.right:
                self.right = PrefixCodeTree.Node()
            return self.right
        
        def getNode(self, i):
            if i == 0:
                return self.getNodeLeft()
            return self.getNodeRight()

        def setSymbol(self, symbol):
            self.symbol = symbol
        
        def getSymbol(self):
            return self.symbol


    def __init__(self):
        self.head = self.Node()
    
    def insert(self, bits, symbol):
        currentNode = self.head
        for bit in bits:
            currentNode = currentNode.getNode(bit)
        
        currentNode.setSymbol(symbol)

    # bytes must be an array of bytes
    def decode(self, bytes, length):
        bits = ''.join(format(byte, '08b') for byte in bytes)[:length]

        decoded = ''

        currentNode = self.head
        for bit in bits:
            currentNode = currentNode.getNode(int(bit))
            if currentNode.getSymbol():
                decoded += currentNode.getSymbol()
                currentNode = self.head
        
        return decoded

# codeTree = PrefixCodeTree()

# codebook = {
#     'x1': [0],
#     'x2': [1,0,0],
#     'x3': [1,0,1],
#     'x4': [1,1]
# }

# for symbol in codebook:
#     codeTree.insert(codebook[symbol], symbol)


# print(codeTree.decode(b'\xd2\x9f\x20', 21))

