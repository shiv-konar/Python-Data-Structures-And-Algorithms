from Nodes import SingleLinkedListNode
"""
head --->1 ---> 2 ---> 3 ----> 4 ---->5 ---> None

"""


class SingleLinkedList:

    """Constructor. Sets the length of the linkedlist to zero and initializes head reference"""
    def __init__(self):
        self.head = None
        self.length = 0

    """ Method to get the length of the list """
    def get_list_length(self):
        return self.length

    """ Method to INSERT a node at the beginning of the list """
    def insert_at_beginning(self, data):
        new_node = SingleLinkedListNode()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    """ Method to INSERT a node at the end of the list """
    def insert_at_end(self, data):
        new_node = SingleLinkedListNode()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.has_next():
                current = current.get_next()
            current.set_next(new_node)
        self.length += 1

    """ Method to INSERT a node at the given position, i.e. after postion - 1 . Position count start at 0 """
    def insert_at_position(self, position, data):
        if position > self.length or position < 0:
            return None
        else:
            if position == 0:
                self.insert_at_beginning(data)
            else:
                if position == self.length:
                    self.insert_at_end(data)
                else:
                    new_node = SingleLinkedListNode()
                    new_node.set_data(data)
                    current = self.head
                    count = 0
                    while count < (position - 1):
                        current = current.get_next()
                        count += 1
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    self.length += 1

    """ Method to INSERT a new node to the list. Default insertion at the end of the list """
    def add(self, data):
        self.insert_at_end(data)

    """ Method to PRINT the elements of the list """
    def print_list(self):
        if self.length == 0:
            print "Linked List is empty"
        else:
            current = self.head
            while current.has_next():
                print str(current.get_data()) + " ---> ",
                current = current.get_next()
            print str(current.get_data())

    """ Method to DELETE the node at the beginning of the list """
    def delete_at_beginning(self):
        if self.length == 0:
            return "List is empty"
        else :
            self.head = self.head.get_Next()
            self.length -= 1

    """ Method to DELETE the node at the end of the list """
    def delete_at_end(self):
        if self.length == 0:
            return "List is empty"
        else:
            current = self.head
            previous = None
            while current.has_next():
                previous = current
                current = current.get_next()
            previous.set_Next(None)
            self.length -= 1

    """ Method to DELETE a node at the given position, i.e. after postion - 1 . Position count start at 0 """
    def delete_at_position(self, position):
        if position > self.length or position < 0:
            return "Position does not exist"
        else:
            if position == 0:
                self.delete_at_beginning()
            elif position == self.length:
                self.delete_at_end()
            else:
                count = 0
                current = self.head
                previous = None
                while count < position:
                    previous = current
                    current = current.get_next()
                    count += 1
                previous.set_next(current.get_next())
                self.length -= 1

    """ Method to DELETE a node with a given value """
    def delete_value(self, value):
        if self.length == 0:
            print " List is empty "
        else:
            current = self.head
            previous = None
            while current.has_next():
                if current.get_data() == value:
                    break
                previous = current
                current = current.get_next()
            if current.get_data() != value:
                print "Item " + str(value) + " not in the list"
            else:
                previous.set_next(current.get_next())
                self.length -= 1

    def delete_node(self, node):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current is node:
                    found = True
                elif current is None:
                    print "Node not in the list"
                    return
                else:
                    previous = current
                    current = current.get_next()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
                self.length -= 1

    """ Method to clear the list """
    def clear(self):
        self.head = None
        self.length = 0

    """ Method to INSERT a node in a sorted linked list """
    def insert_node_in_sorted_list(self, data):
        new_node = SingleLinkedListNode()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            previous = None
            stop = False

            while current is not None and not stop:
                if current.get_data() > data:
                    stop = True
                else:
                    previous = current
                    current = current.get_next()
                if previous is None:
                    new_node.set_next(current)
                    self.head = new_node
                else:
                    new_node.set_next(current)
                    previous.set_next(new_node)
        self.length += 1


def main():
    l = SingleLinkedList()
    l.add(1)
    l.add(3)
    l.add(5)
    l.add(7)
    l.add(9)
    l.add(11)
    l.add(13)
    l.insert_node_in_sorted_list(6)
    l.print_list()

if __name__ == '__main__':
    main()
