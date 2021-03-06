class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если не найден узел,
        # и в дереве только один корень

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None


    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind
        self.find_node = BSTFind()
        if self.Root == None:
            return self.find_node
        else:
            self.find_node.Node = self._FindNodeByKey(key, self.Root)
            if self.find_node.Node != None:
                if self.find_node.Node == self.Root:
                    self.find_node.Node = None
                    self.find_node.NodeHasKey = False
                else:
                    self.find_node.NodeHasKey = True
            else:
                self.find_node.NodeHasKey = False
            return self.find_node


    """
        else:
            self.find_node.Node = self._FindNodeByKey(key, self.Root)
            if self.find_node.Node == None:
                self.find_node.NodeHasKey = False
                return None
            else:
                self.find_node.NodeHasKey = True
                return self.find_node
    """


    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        if self.Root == None:
            self.Root = BSTNode(key, val, None)
            return True
        else:
            if self.FindNodeByKey(key).NodeHasKey == True:
                return False
            else:
                newnode = BSTNode(key, val, None)
                self._AddKeyValue(self.Root, newnode)
                return True


    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        if FindMax == True:
            return self._FindMaximum(FromNode)
        return self._FindMinimum(FromNode)


    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        if self.FindNodeByKey(key).NodeHasKey == False:
            return False # если узел не найден
        else:
            self._DeleteNodeByKey(self._FindNodeByKey(key, self.Root))
            return True


    def Count(self):
        # количество узлов в дереве
        return self._CountNodes(self.Root)


    def _FindNodeByKey(self, key, node):
        if key == node.NodeKey:
            return node
        elif key < node.NodeKey and node.LeftChild is not None:
            return self._FindNodeByKey(key, node.LeftChild)
        elif key > node.NodeKey and node.RightChild != None:
            return self._FindNodeByKey(key, node.RightChild)


    def _AddKeyValue(self, node, newnode):
        while node != None:
            if newnode.NodeKey > node.NodeKey:
                if node.RightChild != None:
                    node = node.RightChild
                else:
                    newnode.Parent = node
                    node.RightChild = newnode
                    break
            elif newnode.NodeKey < node.NodeKey:
                if node.LeftChild != None:
                    node = node.LeftChild
                else:
                    newnode.Parent = node
                    node.LeftChild = newnode
                    break


    def _FindMaximum(self, node):
        if node.RightChild == None:
            return node
        return self._FindMaximum(node.RightChild)


    def _FindMinimum(self, node):
        if node.LeftChild == None:
            return node
        return self._FindMinimum(node.LeftChild)


    def _DeleteNodeByKey(self, node):
        if node.LeftChild != None and node.RightChild != None:
            minNode = self.FinMinMax(node.RightChild, False)
            node.NodeKey = minNode.NodeKey
            node.NodeValue = minNode.NodeValue
            return self._DeleteNodeByKey(minNode)
        elif node.LeftChild != None:
            if node == node.Parent.LeftChild:
                node.Parent.LeftChild = node.LeftChild
            else:
                node.Parent.RightChild = node.LeftChild
            node.LeftChild.Parent = node.Parent
            node = node.LeftChild
        elif node.RightChild != None:
            if node == node.Parent.RightChild:
                node.Parent.RightChild = node.RightChild
            else:
                node.Parent.LeftChild = node.RightChild
            node.RightChild.Parent = node.Parent
            node = node.RightChild
        else:
            if node == node.Parent.LeftChild:
                node.Parent.LeftChild = None
            else:
                node.Parent.RightChild = None
        return node


    def _CountNodes(self, node):
        if node == None:
            count = 0
        else:
            return self._CountNodes(node.LeftChild) + self._CountNodes(node.RightChild) + 1
        return count