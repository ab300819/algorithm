#!/usr/bin/env python3
import unittest

from graph.graph import ListGraph


class TestStringMethods(unittest.TestCase):

    def setUp(self):
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

        self._graph = ListGraph(relation)
        self._graph.create()

    def test_list_graph_bfs(self):
        self.assertEqual(self._graph.bfs(0, 1), [0, 1])
        self.assertEqual(self._graph.bfs(0, 6), [0, 1, 4, 6])

    def test_list_graph_dfs(self):
        self.assertEqual(self._graph.dfs(0, 1), [0, 1])
        self.assertEqual(self._graph.dfs(0, 6), [0, 1, 2, 5, 4, 6])


if __name__ == '__main__':
    unittest.main()
