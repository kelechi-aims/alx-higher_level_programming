#!/usr/bin/python3
""" A class Node that defines a node of a singly linked list.
    A class SinglyLinkedList that defines a singly linked list

"""


class Node:
    """ A class Node that defines a node of a singly linked list. """

    def __init__(self, data, next_node=None):
        """ Initializes a Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list.
                Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not
                a node object or None.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data value of the node.

        Returns:
            int: The data value of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Set the data value of the node.

        Args:
            value (int): The data value of the node.

        Raises:
            TypeError: If value is not an integer.

        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If value is not a Node object or None.

        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ A class that defines a singly linked list. """

    def __init__(self):
        """ Initializes a SinglyLinkedList instance. """
        self.head = None

    def sorted_insert(self, value):
        """ Insert a new Node into the correct sorted position in the list.

        The list is sorted in increasing order.

        Args:
            value (int): The value to be inserted.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and value >= current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """ Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        """
        node = []
        current = self.head
        while current:
            node.append(str(current.data))
            current = current.next_node
        return "\n".join(node)
