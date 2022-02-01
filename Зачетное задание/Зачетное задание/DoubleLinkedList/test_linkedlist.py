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

    def test_del_first_item(self):
        linked_list = LinkedList([1, 2, 3])
        del linked_list[0]
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([2, 3])")
        self.assertEqual(2, len(linked_list))

        self.assertEqual(2, linked_list.head.value)
        self.assertEqual(3, linked_list.tail.value)

    def test_del_last_item(self):
        linked_list = LinkedList([1, 2, 3])
        del linked_list[len(linked_list) - 1]
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([1, 2])")
        self.assertEqual(2, len(linked_list))

        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(2, linked_list.tail.value)

    def test_del_single_item(self):
        linked_list = LinkedList([1])
        del linked_list[0]
        print(linked_list)
        self.assertEqual(repr(linked_list), "LinkedList([])")
        self.assertEqual(0, len(linked_list))

        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

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


class TestDoubleLinkedList(unittest.TestCase):
    def test_init_dll(self):
        dll = DoubleLinkedList([1, 2, 3])

        self.assertEqual(1, dll.head.value)
        self.assertIsInstance(dll.head, DoubleLinkedNode)

        self.assertEqual(3, dll.tail.value)
        self.assertIsInstance(dll.tail, DoubleLinkedNode)

        self.assertEqual(3, len(dll))

    def test_init_empty_dll(self):
        dll = DoubleLinkedList()

        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        self.assertEqual(0, len(dll))
