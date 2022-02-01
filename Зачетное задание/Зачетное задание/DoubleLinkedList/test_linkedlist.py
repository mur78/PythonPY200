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

    def test_insert_list(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.insert(1, 100)
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([1, 100, 2, 3])")

    def test_append_list(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        linked_list.append(90)
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([1, 2, 3, 4, 5, 90])")

    def test_setitem_list(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        linked_list.__setitem__(1, 5)
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([1, 5, 3, 4, 5])")

    def test_list_linked_nodes(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right_node")
        left_node = Node("left_node", next_=right_node)

        self.assertIs(right_node, left_node.next)
        self.assertEqual("left_node", left_node.value)

        self.assertIsNone(right_node.next)
        self.assertEqual("right_node", right_node.value)


