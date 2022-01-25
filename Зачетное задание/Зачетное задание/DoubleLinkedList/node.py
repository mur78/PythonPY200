from typing import Any, Optional

class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
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

    def __repr__(self) -> str:
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        next_node = None if self.next is None else f"DoubleLinkedNode({self.next.value})"
        # todo prev_node
        prev_node = None if self.prev is None else f"DoubleLinkedNode({self.prev.value})"

        return f"DoubleLinkedNode({self.value}, {next_node}, {prev_node})"


    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional['DoubleLinkedNode']):
        self.is_valid(prev_)
        self._prev = prev_


if __name__ == "__main__":

    double_node = DoubleLinkedNode(2, next_=DoubleLinkedNode(3), prev_=DoubleLinkedNode(1))
    print(double_node)
    print(repr(double_node))


