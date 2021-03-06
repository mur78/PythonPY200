from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)


    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

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

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
          # TODO проверка индекса
          if not isinstance(index, int):
              raise TypeError()

          # TODO проверка корректности границ индекса
          if not 0 <= index < self.len:  # для for
              raise IndexError()

    # TODO алгоритм удаления
          if index == 0:
              self.head = self.head.__next
          elif index == self.len - 1:
              t = self.step_by_step_on_nodes(index-1)
              t.next = None
          else:
              p_node = self.step_by_step_on_nodes(index - 1)
              d_node = p_node.next
              next_node = d_node.__next

              self.linked_nodes(p_node, next_node)

          self.len -= 1

    # def index(self, value: Any) -> int:
    #     """
    #     Возвращает индекс переданного значения
    #     :param value:
    #         значение индекс которого нужно получить
    #     :return: int
    #         индекс заданного значения
    #     """
    #     current_node = self.head
    #     if current_node.value == value:
    #         return 0
    #
    #     for i in range(1, self.len):
    #         current_node = current_node.next
    #         if current_node.value == value:
    #             return i

    def count_nodes(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

if __name__ == "__main__":
    # Write your solution here
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    del linked_list[1]
    print(linked_list)

    del linked_list[1]
    print(linked_list)

    del linked_list[0]
    print(linked_list)

