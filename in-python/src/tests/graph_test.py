#!/usr/bin/env python3
import unittest

from graph.graph import ListGraph


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_graph_bfs_1(self):
        relation = [
            (0, 1),
        ]

        graph = ListGraph(relation)
        graph.create()
        self.assertEqual(graph.bfs(0, 2), [])
        self.assertEqual(graph.bfs(0, 1), [0, 1])

    def test_list_graph_bfs_2(self):
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

        graph = ListGraph(relation)
        graph.create()
        self.assertEqual(graph.bfs(0, 6), [0, 1, 4, 6])

    def test_isupper(self):
        pass

    def test_split(self):
        pass


if __name__ == '__main__':
    unittest.main()
