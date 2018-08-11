import queue
# 节点
class Binode(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right =right
# 前序遍历生成Tree
class Bitree(object):
    def __init__(self, queue):
        self.queue = queue
        self.tree = Binode('root')
        self.left = self.tree.left
        self.right =self.tree.right
        self.__prelist = []
        self.__midlist = []
        self.__postlist = []
        self.createBitree()
    # 前序遍历生成Tree
    def createBitree(self):
        self.tree = Binode(self.queue.get())
        self.__createBitree(self.tree, 0, self.queue)
        self.__createBitree(self.tree, 1, self.queue)
    def __createBitree(self, binode, direction, queue):
        nodeData = queue.get()
        if direction == 0:
            if nodeData == '#':
                binode.left = None 
            else:
                binode.left = Binode(nodeData)
                self.__createBitree(binode.left, 0,queue)
                self.__createBitree(binode.left, 1,queue)
        if direction == 1:
            if nodeData == '#':
                binode.right = None 
            else:
                binode.right = Binode(nodeData)
                self.__createBitree(binode.right, 0,queue)
                self.__createBitree(binode.right, 1,queue)   
    # 前序遍历 Tree
    def preOrder(self):
        self.__preOrder(self.tree)
        return self.__prelist
    def __preOrder(self, tree):
        if tree is None:
            self.__prelist.append('#')
        else:
            self.__prelist.append(tree.data)
            self.__preOrder(tree.left)
            self.__preOrder(tree.right)
    
    # 中序遍历 Tree
    def midOrder(self):
        self.__midOrder(self.tree)
        return self.__midlist
    def __midOrder(self, tree):
        if tree is None:
            self.__midlist.append('#')
        else:
            self.__midOrder(tree.left)
            self.__midlist.append(tree.data)
            self.__midOrder(tree.right)

    # 后序遍历 Tree
    def postOrder(self):
        self.__postOrder(self.tree)
        return self.__postlist
    def __postOrder(self, tree):
        if tree is None:
            self.__postlist.append('#')
        else:
            self.__postOrder(tree.left)
            self.__postOrder(tree.right)
            self.__postlist.append(tree.data)


# test
if __name__ =='__main__':
    q = queue.Queue()
    for s in 'AB#D##C##':
        q.put(s)
    tree = Bitree(q)
    print(tree.preOrder())
    print(tree.midOrder())
    print(tree.postOrder())