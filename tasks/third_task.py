# Инвертировать бинарное дерево поиска. Инвертировать дерево – значит прекомпоновать
# его элементы таким образом, чтобы узлы справа от материнского узла были больше, а слева - меньше.

class BinaryTree:

    root = None

    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def __get_latest_node__(self, value, start_node):
        if value > start_node.value and start_node.right is not None:
            return self.__get_latest_node__(value, start_node.right)
        elif value < start_node.value and start_node.left is not None:
            return self.__get_latest_node__(value, start_node.left)
        return start_node

    def __get_latest_node_reversed__(self, value, start_node):
        if value < start_node.value and start_node.right is not None:
            return self.__get_latest_node__(value, start_node.right)
        elif value > start_node.value and start_node.left is not None:
            return self.__get_latest_node__(value, start_node.left)
        return start_node

    def insert_node(self, value, revers=False):
        if self.root is None:
            self.root = self.Node(value)
            return

        if not revers:
            place = self.__get_latest_node__(value, self.root)
            if value < place.value:
                place.left = self.Node(value)
            else:
                place.right = self.Node(value)
        else:
            place = self.__get_latest_node_reversed__(value, self.root)
            if value > place.value:
                place.left= self.Node(value)
            else:
                place.right= self.Node(value)

    def __print_root__(self):
        print("[" + str(self.root.value) + "]")

    def __print_part__(self, node):
        if node == self.root.left:
            print("(" + str(node.value) + "l)")
        elif node == self.root.right:
            print("(" + str(node.value) + "r)")
        if node.left is not None:
            print(str(node.left.value) + "l")
            self.__print_part__(node.left)
        if node.right is not None:
             print(str(node.right.value) + "r")
             self.__print_part__(node.right)

    def __print_reversed_part__(self, node, values):
        if node == self.root.left:
            values.append("(" + str(node.value) + "l)")
        elif node == self.root.right:
            values.append("(" + str(node.value) + "r)")
        if node.left is not None:
            values.append(str(node.left.value) + "l")
            self.__print_part__(node.left)
        if node.right is not None:
            values.append(str(node.right.value) + "r")
            self.__print_part__(node.right)
        return values

    def print_tree(self):
        values = self.__print_reversed_part__(self.root.left, []) # left part
        for value in values[::-1]:
            print(value)
        self.__print_root__()
        self.__print_part__(self.root.right) # right part

    def reverse_tree(self, node):
        if node.left and node.right:
            node.left, node.right = node.right, node.left
            self.reverse_tree(node.left)
            self.reverse_tree(node.right)
        if node.left and node.right is None:
            self.insert_node(node.left.value, revers=True)
            node.left = None
        if node.left is None and node.right:
            self.insert_node(node.right.value, revers=True)
            node.right = None

bt = BinaryTree()
bt.insert_node(5)
bt.insert_node(3)
bt.insert_node(7)
bt.insert_node(8)
bt.insert_node(6)
bt.insert_node(2)
bt.insert_node(1)
bt.insert_node(4)

bt.print_tree()

print()
bt.reverse_tree(bt.root)
bt.print_tree()