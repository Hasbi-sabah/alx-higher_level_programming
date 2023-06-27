#!/usr/bin/python3
"""
Defines a class Node
"""


class Node:
    """
    A class named Node
    """
    def __init__(self, data, next_node=None):
        """
        Initialises instances.

        Args:
            data (int): holds value
            next_node (Node): points to next node, can be null
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Defines a class SinglyLinkedList
"""


class SinglyLinkedList:
    """
    A class named SinglyLinkedList
    """
    def __init__(self):
        """
        initializes a private instance head
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Sorts new value into list
        """
        new = Node(value)
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        temp = self.__head
        while temp.next_node is not None:
            if value < temp.next_node.data:
                break
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new

    def __str__(self):
        """
        Prints list.
        """
        s = ''
        temp = self.__head
        while temp is not None:
            s += str(temp.data)
            if temp.next_node is not None:
                s += '\n'
            temp = temp.next_node
        return s
