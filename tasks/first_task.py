# Задача 1
# Сделать реверс односвязного списка.
# Пример:
# Входные данные: 1, 2, 3, 4, 5
# Результат: 5, 4, 3, 2, 1

# list works like this: each element has a link to the next node and saves a value

class MyLinkedList:

    # internal class for nodes of the list
    class Node:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

        # O(1)
        def add_link_to_next(self, next_node):
            self.next = next_node

    firstElement = None

    # O(n)
    def __get_node_by_index(self, index) -> Node:
        next_element = self.firstElement
        count = 0

        if count == index:
            return next_element

        while count != index and next_element.next is not None:
            count += 1
            next_element = next_element.next
            if count == index:
                return next_element

    def get_by_index(self, index):
        print(self.__get_node_by_index(index).value)

    # O(n)
    def __get_last_node(self) -> Node:
        next_element = self.firstElement

        while next_element.next is not None:
            next_element = next_element.next

        return next_element

    # O(n)
    def get_last(self):
        print(self.__get_last_node().value)

    # O(n)
    def add(self, value):
        new_el = self.Node(value)
        if self.firstElement is None:
            self.firstElement = new_el
        else:
            self.__get_last_node().add_link_to_next(new_el)

    # O(1) or O(n)
    def insert(self, index, value):
        new_node = self.Node(value)

        if index == 0:
            new_node.next = self.firstElement
            self.firstElement = new_node
        else:
            prev_node = self.__get_node_by_index(int(index) - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node

    # O(n)
    def print(self):
        start_element = self.firstElement
        while start_element is not None:
            print(start_element.value, end=" ")
            start_element = start_element.next
        print("")

    # O(n^2)
    def reverse(self):
        last_element = self.__get_last_node()
        prev_element = self.firstElement

        print(last_element.value, end=" ")

        while last_element is not self.firstElement:
            while prev_element.next is not last_element:
                prev_element = prev_element.next

            print(prev_element.value, end=" ")

            last_element = prev_element
            prev_element = self.firstElement


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    myLinkedList.add(1)
    myLinkedList.add(2)
    myLinkedList.add(3)
    myLinkedList.add(4)
    myLinkedList.add(5)
    myLinkedList.print()
    myLinkedList.get_by_index(3)
    myLinkedList.reverse()
    myLinkedList.insert(2, 67)
    print()
    myLinkedList.reverse()
    print()
    myLinkedList.print()
