#!/usr/bin/env python3

class MatrixGraph:
    def __int__(self, node_num: int, node_relation: []):
        self.vex = []
        self.arc = []
        self.node_num = node_num
        self.node_relation = node_relation

    def create(self):
        pass


if __name__ == '__main__':
    node_num = 10
    node_relation = [
        (1, 2),
        (1, 3),
        (1, 5),
    ]
    graph = MatrixGraph(node_num, node_relation)
    print(node_relation)
