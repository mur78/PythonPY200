from typing import Any, Iterable, Optional
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)


    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        #append_node = Node(value)
        append_node = self.CLASS_NODE(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self._linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.__len += 1

    def _step_by_step_on_nodes(self, index: Any) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):  # todo отдельный метод DRY
            raise TypeError()

        if not 0 <= index < self.__len:
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def _linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Метод удаляет значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.__len:
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.__len - 1:
            tail = self.tail  # fixme self.tail
            tail.next = None
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self._linked_nodes(prev_node, next_node)

        self.__len -= 1

    def insert(self, index: int, value: Any) -> None:
        """ Метод вставки узла по индексу. """

        if not isinstance(index, int):
            raise TypeError()
            insert_node = self.CLASS_NODE(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.__len += 1
        elif index >= self.__len - 1:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)

            self.__len += 1

    def index(self, value: Any, start: int = 0, end: int = None) -> int:
        current_node = self.head
        for i in range(self.__len):
            if current_node.value == value:
                return i
            else:
                current_node = current_node.next
        raise ValueError

    def remove(self, value: Any):
        if value in self:
            self.__delitem__(self.index(value))
        else:
            raise ValueError


    def __len__(self) -> int:
        return self.__len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


class DoubleLinkedList(LinkedList):
    """ Класс, который описывает узел связного списка. """
    CLASS_NODE = DoubleLinkedNode


    @staticmethod
    def _linked_nodes(left: DoubleLinkedNode, right: DoubleLinkedNode) -> None:
        left.next = right
        right.prev = left




if __name__ == "__main__":
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    linked_list.remove(2)
    print(linked_list)


    linked_list.insert(3, 100)
    print(linked_list)




