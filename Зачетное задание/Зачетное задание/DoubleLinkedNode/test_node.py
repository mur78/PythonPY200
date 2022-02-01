import unittest

from task import Node, DoubleLinkedNode

class TestNode(unittest.TestCase):
    """Тесты Node"""

    def test_repr_node(self):
        node = Node(3, None)
        self.assertEqual(repr(node), "Node(3, None)")

    def test_repr_link_node(self):
        linked_node = Node(3, Node(7))
        self.assertEqual("Node(3, Node(7))", repr(linked_node))

    def test_str_node(self):
        some_value = 3
        node = Node(some_value)
        self.assertEqual(str(some_value), str(node))

    def test_is_valid_node(self):
        node = Node(3)
        with self.assertRaises(TypeError, msg="Должна быть вызвана ошибка типа данных"):
            node.is_valid(5)


class TestDoubleLinkedNode(unittest.TestCase):

    """Тесты Double_Node"""
    def test_repr_double_node(self):
        double_node = DoubleLinkedNode(3, None, None)
        self.assertEqual(repr(double_node), "DoubleLinkedNode(3, None, None)")

    def test_repr_link_double_node(self):
        linked_double_node = DoubleLinkedNode(2, DoubleLinkedNode(3), DoubleLinkedNode(1))
        self.assertEqual("DoubleLinkedNode(2, DoubleLinkedNode(3), DoubleLinkedNode(1))", repr(linked_double_node))

    def test_str_double_node(self):
        some_d_value = 3
        double_node = DoubleLinkedNode(some_d_value)
        self.assertEqual(str(some_d_value), str(double_node))

    def test_linked_dll_with_node(self):
        with self.assertRaises(TypeError):
            DoubleLinkedNode(3, Node(12), None)

        with self.assertRaises(TypeError):
            DoubleLinkedNode(3, None, Node(12))





