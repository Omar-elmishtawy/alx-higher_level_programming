#!/usr/bin/python3
"""Node for single linked list"""


class Node:
    """class to create node for a singlelinked list

        Args:
            data (int): value to be set in the data for the node
            next_node (Node): object from Node
    """
    def __init__(self, data, next_node=None):
        """Initialization for the object from the class Node """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """to set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        "getter for the next_node"
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        "setter for the next node"
        if isinstance(value, Node) or not value:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    """
    class of the singlylinked list
    """

    def __init__(self):
        """initialization of the obj from sinlgylinkedlit"""
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        temp = self.__head

        if not self.__head:
            self.__head = node
        elif self.__head.data > node.data:
            node.next_node = self.__head
            self.__head = node
        else:
            while temp.next_node and temp.next_node.data < node.data:
                temp = temp.next_node
            node.next_node = temp.next_node
            temp.next_node = node

    def __str__(self):
        value = []
        tmp = self.__head

        while tmp:
            value.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(value)
