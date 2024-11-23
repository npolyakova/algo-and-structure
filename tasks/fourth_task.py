# Реализовать балансировку красно-черного дерева.
# 1. Каждый узел промаркирован красным или чёрным цветом
# 2. Корень и конечные узлы (листья) дерева — чёрные
# 3. У красного узла родительский узел — чёрный
# 4. Все простые пути из любого узла x до листьев содержат одинаковое количество чёрных узлов
# 5. Чёрный узел может иметь чёрного родителя

class RBTree:

    def __init__(self):
        self.null = self.Node(None, 'black')
        self.root = self.null

    class Node:
        def __init__(self, value, color='red'):
            self.value = value
            self.color = color
            self.left = None
            self.right = None
            self.parent = None

    def __new_node__(self, new_node):
        current = self.root
        parent = None

        while current != self.null:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def insert(self, data):
        new_node = self.Node(data)
        new_node.left = self.null
        new_node.right = self.null
        self.__new_node__(new_node)
        self._balance(new_node)

    def _balance(self, new_node):
        while new_node != self.root and new_node.parent.color == 'red':         # Пока новый узел не является корнем и родитель - красный
            if new_node.parent == new_node.parent.parent.left:                  # Берем левое поддерево за родителя
                uncle = new_node.parent.parent.right                            # Дядя - правое поддерево, тогда
                if uncle.color == 'red':                                        # 1) дядя красный
                    new_node.parent.color = 'black'                             # Красим родителя и дядю - в черный, дедушку - в красный
                    uncle.color = 'black'
                    new_node.parent.parent.color = 'red'
                    new_node = new_node.parent.parent                           # Если новый узел - это дедушка, то
                else:                                                           # 2) дядя черный
                    if new_node == new_node.parent.right:                       # Если новый узел - это правое поддерево
                        new_node = new_node.parent                              # Поднимаемся к родителю и делаем левый поворот
                        self._left_rotate(new_node)
                    new_node.parent.color = 'black'                             # Красим родителя в черный, дедушку в красный + правый поворот
                    new_node.parent.parent.color = 'red'
                    self._right_rotate(new_node.parent.parent)
            else:                                                               # Когда родитель - правое поддерево
                uncle = new_node.parent.parent.left                             # Дядя - правое поддерево и может быть 2 случая
                if uncle.color == 'red':                                        # 1) дядя красный
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.parent.parent.color = 'red'
                    new_node = new_node.parent.parent
                else:                                                           # 2) дядя черный
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    new_node.parent.color = 'black'
                    new_node.parent.parent.color = 'red'
                    self._left_rotate(new_node.parent.parent)

        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null:
            y.left.parent = x
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.null:
            x.right.parent = y
        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def height(self):
        def _height(node):
            if node == self.null:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def __fill__(self, result, node, index):      # Заполнение узлов по уровням
        if node != self.null:
            result[index] = node
            self.__fill__(result, node.left, 2 * index + 1)
            self.__fill__(result, node.right, 2 * index + 2)

    def __print_root__(self):
        print("[" + str(self.root.value) + " " + str(self.root.color) + "]")

    def __print_part__(self, node):
        if node == self.root.left:
            print("(" + str(node.value) + " " + str(node.color) + " l)")
        elif node == self.root.right:
            print("(" + str(node.value) + " "  + str(node.color) + " r)")
        if node.left is not None:
            print(str(node.left.value) + " "  + str(node.color))
            self.__print_part__(node.left)
        if node.right is not None:
            print(str(node.right.value) + " "  + str(node.color))
            self.__print_part__(node.right)

    def __print_reversed_part__(self, node, values):
        if node == self.root.left:
            values.append("(" + str(node.value) + " "  + str(node.color) + " l)")
        elif node == self.root.right:
            values.append("(" + str(node.value) + " "  + str(node.color) + " r)")
        if node.left is not None:
            values.append(str(node.left.value) + " " + str(node.color) + " l")
            self.__print_part__(node.left)
        if node.right is not None:
            values.append(str(node.right.value) + " "  + str(node.color) + " r")
            self.__print_part__(node.right)
        return values

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        values = self.__print_reversed_part__(self.root.left, [])
        for value in values[::-1]:
            print(value)
        self.__print_root__()
        self.__print_part__(self.root.right)


if __name__ == '__main__':
    rbt = RBTree()
    data_list = [17, 3, 18, 100, 2, 8, 11, 37]

    for data in data_list:
        rbt.insert(data)

    rbt.print_tree()
