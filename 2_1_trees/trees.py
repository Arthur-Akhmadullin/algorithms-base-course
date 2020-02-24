class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None


    def AddChild(self, ParentNode, NewChild):
        #pass # ваш код добавления нового дочернего узла существующему ParentNode
        '''
        if ParentNode is None:
            self.Root = NewChild
        elif NewChild not in ParentNode.Children \
                and NewChild.Parent == ParentNode:
            ParentNode.Children.append(NewChild)
        '''
        if self.Root is None:
            self.Root = NewChild
        elif ParentNode and NewChild not in ParentNode.Children:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)




    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        if NodeToDelete is not self.Root:
            if len(NodeToDelete.Children) > 0:
                for children in NodeToDelete.Children:
                    children.Parent = NodeToDelete.Parent
                    NodeToDelete.Parent.Children.append(children)
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            NodeToDelete.Children.clear()



    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        array = []
        if self.Root is not None:
            array = self.RecursiveGetAllNodes(self.Root)
        return array



    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        '''
        if self.Root is not None:
            return self.RecursiveFindNodes(self.Root, val)
        '''
        array = []
        for node in self.GetAllNodes():
            if node.NodeValue == val:
                array.append(node)
        return array


    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent



    def Count(self):
        # количество всех узлов в дереве
        '''
        count = 0
        if self.Root is not None:
            count = self.RecursiveTraversalForDefCount(self.Root)
        return count
        '''
        return len(self.GetAllNodes())



    def LeafCount(self):
        '''
        lcount = 0
        if self.Root is not None:
            lcount = self.RecursiveTraversal(self.Root)
        return lcount
        '''
        # количество листьев в дереве
        lcount = 0
        for node in self.GetAllNodes():
            if node.Children == []:
                lcount += 1
        return lcount


    def FindNodeLevel(self):
        keys = self.RecursiveGetAllNodes(self.Root)
        level = self.RecursiveTraversalForFindNodeLevel(self.Root, 0)
        dict_level = dict(zip(keys, level))
        return dict_level

    '''
    Рекурсиные функции использовались до создания функции GetAllNodes().
    После подсчета узлов и листьев, а также поиска по значению с помощью GetAllNodes()
    закомментировал за ненадобностью.
    
    
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
    '''


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


    def EvenTrees(self):
        list_remove_edges = []
        if self.Count() % 2 != 0:
            return
        else:
            return self.RecursiveEvenTrees(self.Root)
            #return []


    def RecursiveEvenTrees(self, node):
        edge = []
        if node.Children != []:
            for children in node.Children:
                if len(self.RecursiveGetAllNodes(children)) % 2 == 0:
                    #edge.append(node.NodeValue)
                    #edge.append(children.NodeValue)
                    edge.append(node)
                    edge.append(children)
                edge += self.RecursiveEvenTrees(children)
        return edge