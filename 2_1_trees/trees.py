class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None


    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        elif NewChild not in ParentNode.Children \
                and NewChild.Parent == ParentNode:
            ParentNode.Children.append(NewChild)
        #pass # ваш код добавления нового дочернего узла существующему ParentNode


    def DeleteNode(self, NodeToDelete):
        #ДОБАВИТЬ БЛОК TRY EXCEPT - ПОПЫТКА УДАЛЕНИЯ КОРНЕВОГО УЗЛА
        if NodeToDelete is not self.Root:
            if len(NodeToDelete.Children) > 0:
                for children in NodeToDelete.Children:
                    children.Parent = NodeToDelete.Parent
                    NodeToDelete.Parent.Children.append(children)
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            NodeToDelete.Children.clear()
        #pass # ваш код удаления существующего узла NodeToDelete


    def GetAllNodes(self):
        if self.Root is not None:
            return self.RecursiveGetAllNodes(self.Root)
        # ваш код выдачи всех узлов дерева в определённом порядке
        #pass


    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if self.Root is not None:
            return self.RecursiveFindNodes(self.Root, val)


    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        #pass


    def Count(self):
        # количество всех узлов в дереве
        count = 0
        if self.Root is not None:
            count = self.RecursiveTraversalForDefCount(self.Root)
        return count


    def LeafCount(self):
        lcount = 0
        if self.Root is not None:
            lcount = self.RecursiveTraversal(self.Root)
        return lcount
        # количество листьев в дереве


    def FindNodeLevel(self):
        keys = self.RecursiveGetAllNodes(self.Root)
        level = self.RecursiveTraversalForFindNodeLevel(self.Root, 0)
        dict_level = dict(zip(keys, level))
        return dict_level


    def RecursiveTraversal(self, Node):
        leaf_count = 0
        if Node.Children:
            for children in Node.Children:
                leaf_count += self.RecursiveTraversal(children)
        else:
            leaf_count += 1
        return leaf_count


    def RecursiveTraversalForDefCount(self, Node):
        count = 0
        if Node.Children:
            count += 1
            for children in Node.Children:
                count += self.RecursiveTraversal(children)
        else:
            count += 1
        return count


    def RecursiveFindNodes(self, Node, value):
        array = []
        if Node.NodeValue == value:
            array.append(Node)
        if Node.Children:
            for children in Node.Children:
                array += (self.RecursiveFindNodes(children, value))
        return array


    def RecursiveGetAllNodes(self, Node):
        array = []
        array.append(Node)
        if Node.Children:
            for children in Node.Children:
                array += self.RecursiveGetAllNodes(children)
        return array


    def RecursiveTraversalForFindNodeLevel(self, Node, level):
        array_level = []
        array_level.append(level)
        if Node.Children:
            level += 1
            for children in Node.Children:
                array_level += self.RecursiveTraversalForFindNodeLevel(children, level)
        return array_level




