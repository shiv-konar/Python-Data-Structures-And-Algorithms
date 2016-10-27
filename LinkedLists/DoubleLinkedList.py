from Nodes import DoubleLinkedListNode
"""
head --->1 <---> 2 <---> 3 <----> 4 <---->5 <--- tail
                                          ᛎ
                                          None
"""


class DoubleLinkedList:
    """Constructor. Initializes the list, its length, head and tail references"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """ Method to get the length of the list"""
    def get_list_length(self):
        print self.length

    """ Method to print the elements of the list """
    def print_list(self):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            while current.has_next():
                print str(current.get_data()) + " <---> ",
                current = current.get_next()
            print str(current.get_data())

    """ Method to INSERT a new node at the beginning of the list """
    def insert_at_beginning(self, data):
        new_node = DoubleLinkedListNode()
        new_node.set_data(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        self.length += 1

    """ Method to INSERT a new node at the end of the list """
    def insert_at_end(self, data):
        new_node = DoubleLinkedListNode()
        new_node.set_data(data)

        if self.length is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    """ Method to add a new element to the list. Default insert at the end """
    def add(self, data):
        self.insert_at_end(data)

    """ Method to DELETE the node at the beginning of the list """
    def delete_at_beginning(self):
        if self.length == 0:
            print "List is empty"
        else:
            temp = self.head
            self.head = self.head.get_next()
            temp.set_next(None)
            self.head.set_prev(None)
            self.length -= 1

    """ Method to DELETE the node at the end of the list """
    def delete_at_end(self):
        if self.length == 0:
            print "List is empty"
        else:
            temp = self.tail
            self.tail = self.tail.get_prev()
            temp.set_prev(None)
            self.tail.set_next(None)
            self.length -= 1

    """ Method to DELETE the node, given the value of the node """
    def delete_value(self, value):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            while current is not None:
                if current.get_data() == value:
                    break
                else:
                    current = current.get_next()
            if current is None:
                print "Value not found in the list"
            else:
                temp = current.get_prev()
                temp.set_next(current.get_next())
                current.get_next().set_prev(temp)
                self.length -= 1

    """ Method to DELETE the node, given the position of the node """
    def delete_at_position(self, position):
        if position + 1 > self.length or position < 0:
            print "Invalid position"
        else:
            if position == 0:
                self.delete_at_beginning()
            else:
                if position + 1 == self.length:
                    self.delete_at_end()
                else:
                    count = 0
                    current = self.head
                    previous = None
                    while count <= position - 1:
                        previous = current
                        current = current.get_next()
                        count += 1
                    previous.set_next(current.get_next())
                    current.get_next().set_prev(previous)
                    current.set_prev(None)
                    current.set_next(None)
                    self.length -= 1

    """ Method to clear the list """
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0


def main():
    l = DoubleLinkedList()
    l.print_list()
    l.insert_at_beginning(1)
    l.insert_at_beginning(2)
    l.insert_at_end(3)
    l.insert_at_end(4)
    l.add(5)
    l.add(6)
    l.print_list()
    l.delete_at_beginning()
    l.print_list()
    l.delete_at_beginning()
    l.print_list()
    l.delete_at_end()
    l.print_list()
    l.delete_at_end()
    l.print_list()
    l.add(5)
    l.add(6)
    l.add(7)
    l.add(8)
    l.print_list()
    l.delete_value(6)
    l.print_list()
    l.delete_at_position(4)
    l.print_list()
    l.delete_at_position(4)
    l.print_list()


if __name__ == '__main__':
    main()
