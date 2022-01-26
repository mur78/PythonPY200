from typing import Any, Iterable, Optional

from node import Node

from collections.abc import MutableSequence

from typing import Any

class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self._linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
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
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Метод удаляет значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self._linked_nodes(prev_node, next_node)

        self.len -= 1

        def insert(self, index: int, value: Any) -> None:
            """ Метод вставки узла по индексу. """

            if not isinstance(index, int):
                raise TypeError()

            insert_node = Node(value)

            if index == 0:
                insert_node.next = self.head
                self.head = insert_node
                self.len += 1
            elif index >= self.len - 1:
                self.append(value)
            else:
                prev_node = self.step_by_step_on_nodes(index - 1)
                next_node = prev_node.next

                self._linked_nodes(prev_node, insert_node)
                self._linked_nodes(insert_node, next_node)

                self.len += 1

    def __len__(self) -> int:
        return self.len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"



class DoubleLinkedList(LinkedList):
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any,
                 next_: Optional['DoubleLinkedNode'] = None,
                 prev_: Optional['DoubleLinkedNode'] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        :param prev_: предыдущий узел, если он есть
        """
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self._prev = prev_

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    def __repr__(self) -> str:
        return f'DoubleLinkedNode({self.value}, next_={None}, prev={None})'




if __name__ == "__main__":
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    linked_list.insert(100, 100)
    print(linked_list)
