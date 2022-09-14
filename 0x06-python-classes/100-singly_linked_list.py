#!/usr/bin/python3
"""Module Node

Raises:
    TypeError: checks if data is an integer
    TypeError: checks if next_node is a Node type

Returns:
    int, node: the content of the data and next_node
"""


class Node:
    def __init__(self, data, next_node=None):
        """Initializes an instance of this class

        Args:
            data (int): the integer to be added
            next_node (Node, optional): next node to be added to the node.
                Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """accessor to the value of the list

        Returns:
            int: the value on the current list
        """
        return self.__data

    @data.setter
    def data(self, value):
        """the data setter

        Args:
            value (int): the value to be added to the list

        Raises:
            TypeError: checks that the data added is an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """accessor to the next node

        Returns:
            Node : the node that the present node points to
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """to set the next node

        Args:
            value (Node): the node that the present node points to

        Raises:
            TypeError: makes sure that value is a Node
        """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    """SinglyLinkedList is a child of the Node class

    Args:
        Node (Node): the main idea behind the singly linked list
    """

    def __init__(self):
        """initializes an instance of this class
        """
        self.__head = None

    def __str__(self):
        """handles the printing of the instance

        Returns:
            str: the contents of the list
        """
        print_val = ''
        head = self.__head
        while head:
            if self.data is not None:
                print_val += self.data + '\n'
            head = self.next_node
        return print_val

    def sorted_insert(self, value):
        """adds a node to the linked list in a sorted way

        Args:
            value (int): the value to be added to the new node
        """
        if self.__head is None:
            self.__head = Node(value)
        elif value <= self.__head.data:
            self.__head = Node(value, self.__head)
        elif value > self.__head.data:
            buffer = self.__head
            while buffer:
                if not buffer.ddnext_node:
                    buffer.next_node = Node(value)
                    break
                elif value < buffer.next_node.data:
                    buffer.next_node = Node(value, buffer.next_node)
                    break
                buffer = buffer.next_node
