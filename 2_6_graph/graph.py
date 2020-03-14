class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size


    # здесь и далее, параметры v -- индекс вершины в списке  vertex
    def AddVertex(self, v):
        # добавление новой вершины со значением value
        # в свободное место массива vertex
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break


    def RemoveVertex(self, v):
        # удаление вершины со всеми её рёбрами
        # в качестве параметра получает индекс удаляемой вершины
        if self.vertex[v] is not None:
            for index_v in range(len(self.vertex)):
                if self.IsEdge(v, index_v) is True:
                    self.RemoveEdge(v, index_v)
            self.vertex[v] = None


    def IsEdge(self, v1, v2):
        # True, если есть ребро между вершинами v1 и v2
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
                return True
            else:
                return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1


    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0


    def DepthFirstSearch(self, VFrom, VTo):
        stack = []
        for v in self.vertex:
            v.Hit = False
        return self.RecursiveDepthFirstSearch(self.vertex[VFrom], self.vertex[VTo], stack, True)
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету



    def RecursiveDepthFirstSearch(self, VFrom, VTo, stack, flagPushStack):
        VFrom.Hit = True
        if flagPushStack is True:
            stack.append(VFrom)

        if len(stack) > 2:
            indexHead = self.vertex.index(stack[0])
            indexTail = self.vertex.index(stack[-1])
            if self.IsEdge(indexHead, indexTail) is True:
                stack.clear()
                stack.append(self.vertex[indexHead])
                stack.append(self.vertex[indexTail])

        if self.SearchTargetVertex(VFrom, VTo):
            stack.append(self.SearchTargetVertex(VFrom, VTo))
            return stack
        elif self.SearchAdjacentVertex(VFrom):
            return self.RecursiveDepthFirstSearch(self.SearchAdjacentVertex(VFrom), VTo, stack, True)
        else:
            stack.pop()
            if stack == []:
                return stack
            else:
                #return self.SearchTargetVertex(stack[-1], VTo)
                return self.RecursiveDepthFirstSearch(stack[-1], VTo, stack, False)



    def SearchTargetVertex(self, VFrom, VTo):
        for i in range(len(self.vertex)):
            if self.IsEdge(self.vertex.index(VFrom), i) is True and \
                    self.vertex[i] is VTo and self.vertex[i].Hit is False:
                # ДОБАВИЛ self.vertex[i].Hit is False
                #stack.append(v)
                #return stack
                return self.vertex[i]
        return None


    def SearchAdjacentVertex(self, VFrom):
        for i in range(len(self.vertex)):
            if self.IsEdge(self.vertex.index(VFrom), i) is True and \
                    self.vertex[i].Hit is False:
                return self.vertex[i]
        return None

    '''
        def PopStack(self, stack):
            stack.pop()
            if stack == []:
                return None
            return stack[-1]
    '''