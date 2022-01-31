import unittest

from task import Node, DoubleLinkedNode, LinkedList, DoubleLinkedList

class TestLinkedList(unittest.TestCase):
    """Тесты LinkedList"""

    def test_del_from_empty_list(self):
        empty_list = LinkedList([])
        with self.assertRaises(IndexError, msg="Удаление LinkedList"):
            del empty_list[0]  # self.AssertRaises(IndexError)

    def test_del_list(self):
        linked_list = LinkedList([1, 2, 3])
        del linked_list[1]
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([1, 3])")

