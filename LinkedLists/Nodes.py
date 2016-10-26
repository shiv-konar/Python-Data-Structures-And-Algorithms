class SingleLinkedListNode:
    """ Constructor initializes the data field and next node pointer """
    def __init__(self):
        self.data = None
        self.next = None

    """ Method for setting the data field of the node """
    def set_data(self, data):
        self.data = data

    """ Method for getting the data field of the node """
    def get_data(self):
        return self.data

    """ Method for setting the next field of the node """
    def set_next(self, next):
        self.next = next

    """ Method for getting the next field of the node """
    def get_next(self):
        return self.next

    """Method for checking if the current node points to another node """
    def has_next(self):
        return self.next != None

    """ Magic method to print the value of the node """
    def __str__(self):
        return "SLL Node: Value {0}".format(self.get_data())


class DoubleLinkedListNode:
    """Constructor initializes the data field and next and previous node pointers"""
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    """ Method to set the data field of the node """
    def set_data(self, data):
        self.data = data

    """ Method to get the data field of the node """
    def get_data(self):
        return self.data

    """ Method to set the next field of the node """
    def set_next(self, next):
        self.next = next

    """ Method to get the next field of the node """
    def get_next(self):
        return self.next

    """ Method to check if the node is pointing to another node """
    def has_next(self):
        return self.next != None

    """ Method to set the previous field of the node """
    def set_prev(self, prev):
        self.prev = prev

    """ Method to get the previous field of the node """
    def get_prev(self):
        return self.prev

    """ Method to check if the node is pointing to a previous node """
    def has_prev(self):
        return self.prev != None

    """ Magic method to print the value of the node """
    def __str__(self):
        return "DLL Node: Value {0}".format(self.get_data())
