"""
数据结构： 树
父节点：具有一个或多个子节点的节点。
子节点：具有父节点的节点。
叶子节点：没有任何子节点的节点
"""


class BinaryTree:
    def __init__(self, rootObj):
        self.value = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, Node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(Node)
        else:
            temp = BinaryTree(Node)
            temp.leftChild, self.leftChild = self.leftChild, temp

    def insertRight(self, Node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(Node)
        else:
            temp = BinaryTree(Node)
            temp.rightChild, self.rightChild = self.rightChild, temp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value


"""前序遍历，递归写法"""


def preOrder(tree: BinaryTree) -> list:
    res = []

    def dfs(Tree):
        if not Tree:
            return
        res.append(Tree.value)
        dfs(Tree.leftChild)
        dfs(Tree.rightChild)

    dfs(tree)
    return res


root = BinaryTree(1)
print(root.getValue())
root.insertLeft(2)
root.insertRight(3)
root.insertLeft(4)
root.insertRight(5)

print(preOrder(root))

print(root)
