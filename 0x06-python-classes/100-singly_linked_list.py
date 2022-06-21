#!/usr/bin/python3
"""
A Singly Linked List module
"""


class Node:
    """
    A class used to represent a node

    Attributes:
        data (int): where the data is stored
        next_node (obj): where the next_node is stored
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node

        Args:
        data (int): data to be added to node
        next_node (obj): points to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get and set data of the node

        Args:
        value (int): data to be stored

        Raises:
            TypeError: if value is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Get and set next node

        Args:
        value (obj): next node

        Raises:
            TypeError: if value is not a Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class used to represent a singly linked list

    Attributes:
        head (obj): where the head node is stored
    """

    def __init__(self):
        """
        Initializes a singly linked list

        Args:
            head (obj): points to the head node
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the linked list

        Args:
            value (int): data to be added
        """
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        elif(self.__head.data >= newNode.data):
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while current.next_node and newNode.data > current.next_node.data:
                current = current.next_node

            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        """
        print class
        """
        res = ""
        ptr = self.__head
        while ptr:
            res += str(ptr.data) + '\n'
            ptr = ptr.next_node
        res = res.strip('\n')
        if len(res):
            return res
        else:
            return ''
