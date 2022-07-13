#!/usr/bin/env python3

from queue import Queue


# 邻接矩阵表示法
class MatrixGraph:
    def __init__(self, node_relation: []):
        self._node_relation = node_relation
        self._arc = []
        self._node_list = []
        self._node_map = {}
        self._found = False

    def create(self):
        node_tuple = ()
        for i in self._node_relation:
            node_tuple = node_tuple + i
        self._node_list = list(set(node_tuple))
        self._node_map = {node: index for index, node in enumerate(self._node_list)}

        self._arc = [[None for i in range(len(self._node_list))] for i in range(len(self._node_list))]
        for i in self._node_relation:
            node_x = self._node_map[i[0]]
            node_y = self._node_map[i[1]]
            self._arc[node_x][node_y] = 1
            self._arc[node_y][node_x] = 1

    def bfs(self, source: int, target: int):

        source_index = self._node_map[source]
        target_index = self._node_map[target]

        path = []
        if source_index == target_index:
            return path
        visited = {key: False for key in range(len(self._node_list))}
        queue = Queue(len(self._node_list))
        queue.put(source_index)

        prev = {key: -1 for key in range(len(self._node_list))}
        while not queue.empty():
            node = queue.get()
            for j in range(len(self._node_list)):
                if self._arc[node][j] == 1 and not visited[j]:
                    prev[j] = node
                    if j == target_index:
                        self._print(prev, source_index, target_index, path)
                        return path
                    visited[j] = True
                    queue.put(j)
        return self._convert_to_node(path)

    def dfs(self, source: int, target: int):

        source_index = self._node_map[source]
        target_index = self._node_map[target]

        visited = {key: False for key in range(len(self._node_list))}
        prev = {key: -1 for key in range(len((self._node_list)))}
        path = []
        self._dfs_reserve(source_index, target_index, visited, prev)
        self._print(prev, source_index, target_index, path)
        return self._convert_to_node(path)

    def _dfs_reserve(self, source_index: int, target_index: int, visited: {}, prev: {}):
        if self._found:
            return
        visited[source_index] = True
        if source_index == target_index:
            self._found = True
            return
        for i in range(len(self._node_list)):
            if not visited[i] and self._arc[source_index][i] == 1:
                prev[i] = source_index
                self._dfs_reserve(i, target_index, visited, prev)

    def _print(self, prev: {}, source: int, target: int, path: {}):
        if prev[target] != -1 and source != target:
            self._print(prev, source, prev[target], path)
        path.append(target)

    def _convert_to_node(self, path: []):
        if not path:
            return path

        result = []
        for i in path:
            result.append(self._node_list[i])
        return result

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
        path = []
        if source == target:
            return path
        visited = {key: False for key in self._arc.keys()}
        queue = Queue(len(self._arc))
        queue.put(source)

        prev = {key: -1 for key in self._arc.keys()}
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
    node_num = 8
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
    matrix_graph = MatrixGraph(relation)
    matrix_graph.create()
    matrix_bfs_path = matrix_graph.bfs(0, 6)
    print(matrix_bfs_path)
    matrix_dfs_path = matrix_graph.dfs(0, 6)
    print(matrix_dfs_path)

    list_graph = ListGraph(relation)
    list_graph.create()
    list_bfs_path = list_graph.bfs(0, 6)
    print(list_bfs_path)

    list_dfs_path = list_graph.dfs(0, 6)
    print(list_dfs_path)
