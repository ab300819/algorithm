#!/usr/bin/env python3

from queue import Queue


# 邻接矩阵表示法
class MatrixGraph:
    def __init__(self, node_num: int, node_relation: []):
        self._arc = []
        self._node_num = node_num
        self._node_relation = node_relation

    def create(self):
        self._arc = [[None for i in range(self._node_num)] for i in range(self._node_num)]
        for i in self._node_relation:
            self._arc[i[0]][i[1]] = 1

    def get_graph(self):
        return self._arc


# 邻接链表表示法
class ListGraph:
    def __init__(self, node_relation: []):
        self._node_relation = node_relation
        self._arc = {}
        self._found = False

    def create(self):
        for i in self._node_relation:
            if i[0] in self._arc:
                self._arc[i[0]].append(i[1])
            else:
                self._arc[i[0]] = [i[1]]

            if i[1] in self._node_relation:
                self._arc[i[1]].append(id[0])
            else:
                self._arc[i[1]] = [i[0]]

    # 广度优先算法
    def bfs(self, source: int, target: int):
        if source == target:
            return
        visited = {key: False for key in self._arc.keys()}
        queue = Queue(len(self._arc))
        queue.put(source)

        prev = {key: -1 for key in self._arc.keys()}
        path = []
        while not queue.empty():
            current = queue.get()
            for i in self._arc[current]:
                if not visited[i]:
                    prev[i] = current
                    if i == target:
                        self._print(prev, source, target, path)
                        return path
                    visited[i] = True
                    queue.put(i)
        return path

    # 深度优先算法
    def dfs(self, source: int, target: int):
        self._found = False
        visited = {key: False for key in self._arc.keys()}
        prev = {key: -1 for key in self._arc.keys()}
        path = []
        self._dfs_reserve(source, target, visited, prev)
        self._print(prev, source, target, path)
        return path

    def _dfs_reserve(self, source: int, target: int, visited: {}, prev: {}):
        if self._found:
            return
        visited[source] = True
        if source == target:
            self._found = True
            return
        for i in self._arc[source]:
            if not visited[i]:
                prev[i] = source
                self._dfs_reserve(i, target, visited, prev)

    def _print(self, prev: {}, source: int, target: int, path: []):
        if prev[target] != -1 and source != target:
            self._print(prev, source, prev[target], path)
        path.append(target)

    def get_graph(self):
        return self._arc


if __name__ == '__main__':
    node_num = 6
    relation = [
        (0, 1),
        (0, 3),
        (1, 2),
        (1, 4),
        (2, 5),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)
    ]
    # graph = MatrixGraph(node_num, relation)
    # graph.create()
    # node_graph = graph.get_graph()
    # for i in node_graph:
    #     print(i)

    graph = ListGraph(relation)
    graph.create()
    bfs_path = graph.bfs(0, 6)
    print(bfs_path)

    dfs_path = graph.dfs(0, 6)
    print(dfs_path)
