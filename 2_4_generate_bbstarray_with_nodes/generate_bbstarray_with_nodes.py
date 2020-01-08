class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла

class BalancedBST:

    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, a):
        return self._GenerateTree(sorted(a), 0, len(a)-1, None, 1)
    # создаём дерево с нуля из неотсортированного массива a
    # ...


    def IsBalanced(self, root_node):
        #return self._checkBalance(root_node) != -1
        return (root_node is None) or (self.IsBalanced(root_node.LeftChild) and
                                     self.IsBalanced(root_node.RightChild) and
        abs(self._checkHeight(root_node.LeftChild) - self._checkHeight(root_node.RightChild)) <= 1)


    def _checkBalance(self, node):
        if node is None:
            return 0

        left = self._checkBalance(node.LeftChild)
        if left == -1:
            return -1
        right = self._checkBalance(node.RightChild)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)


    def _checkHeight(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._checkHeight(node.LeftChild), self._checkHeight(node.RightChild))


    def _GenerateTree(self, array, start, end, parent, level):
        if end < start:
            return None

        middle = (start + end + 1) // 2

        node = BSTNode(array[middle], parent)
        node.Level = level

        if self.Root is None:
            self.Root = node

        level += 1
        node.LeftChild = self._GenerateTree(array, start, middle-1, node, level)
        node.RightChild = self._GenerateTree(array, middle+1, end, node, level)

        return node