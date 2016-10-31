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

    """ Method to find nth node from the end of list using multiple iterations """
    def find_nth_node_from_end_solution1(self, n):
        if self.length < n:
            print "Length of list less than " + str(n)
        elif self.length == n:
            print str(self.head.get_data())
        elif n == 0:
            print "Position n should start from 1"
        else:
            count = 0
            current = self.head
            nth_pointer = self.head
            while count < n - 1:
                current = current.get_next()
                count += 1
            while current.has_next():
                current = current.get_next()
                nth_pointer = nth_pointer.get_next()
            print nth_pointer.get_data()

    """ Method to find the nth node from the end of the list using hash map """
    def find_nth_node_from_end_solution2(self, n):
        if self.length < n:
            print "Length of list less than " + str(n)
        elif self.length == n:
            print str(self.head.get_data())
        elif n == 0:
            print "Position n should start from 1"
        else:
            internal_dictionary = {}
            current = self.head
            index = 1
            while current is not None:
                internal_dictionary[index] = current
                index += 1
                current = current.get_next()
            print str(internal_dictionary[len(internal_dictionary) - n + 1].get_data())

    """ Method to find the nth node from the end of the list in a single scan """
    def find_nth_node_from_end_solution3(self, n):
        if self.length < n:
            print "Length of list less than " + str(n)
        elif self.length == n:
            print str(self.head.get_data())
        elif n == 0:
            print "Position n should start from 1"
        else:
            nth_node_position = self.length - n + 1
            count = 1
            nth_node = self.head
            while count < nth_node_position:
                nth_node = nth_node.get_next()
                count += 1
            print str(nth_node.get_data())


def main():
    l = SingleLinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.add(7)
    l.print_list()
    l.find_nth_node_from_end_solution1(3)
    l.find_nth_node_from_end_solution2(3)
    l.find_nth_node_from_end_solution3(3)


if __name__ == '__main__':
    main()
