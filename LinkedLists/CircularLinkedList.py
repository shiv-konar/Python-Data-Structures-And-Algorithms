from Nodes import SingleLinkedListNode


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def print_list(self):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            print str(current.get_data()),
            current = current.get_next()
            while current is not self.head:
                print str(current.get_data()),
                current = current.get_next()
            print

    def insert_at_beginning(self, data):
        new_node = SingleLinkedListNode()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
            new_node.set_next(self.head)
        else:
            current = self.head
            while current.get_next() is not self.head:
                current = current.get_next()
            new_node.set_next(self.head)
            current.set_next(new_node)
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        if self.length == 0:
            self.insert_at_beginning(data)
        else:
            new_node = SingleLinkedListNode()
            new_node.set_data(data)
            current = self.head
            while current.get_next() is not self.head:
                current = current.get_next()
            new_node.set_next(self.head)
            current.set_next(new_node)
            self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            while current.get_next() is not self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
            self.length -= 1

    def delete_at_end(self):
        if self.length == 0:
            print "List is empty"
        else:
            previous = None
            current = self.head
            while current.get_next() is not self.head:
                previous = current
                current = current.get_next()
            previous.set_next(self.head)
            self.length -= 1

    def delete_at_position(self, position):
        if position > self.length - 1 or position < 0:
            print "Invalid position"
        else:
            if position == 0:
                self.delete_at_beginning()
            elif position == self.length - 1:
                self.delete_at_end()
            else:
                count = 0
                current = self.head
                while count < position - 1:
                    current = current.get_next()
                    count += 1
                current.set_next(current.get_next().get_next())
                self.length -= 1

    def delete_value(self, value):
        if self.length == 0:
            print "List is empty"
        else:
            current = self.head
            position = 0
            while current.get_next() is not self.head:
                if current.get_data() == value:
                    break
                current = current.get_next()
                position += 1
            if current.get_data() != value:
                print "Item not in the list"
            else:
                self.delete_at_position(position)


def main():
    c = CircularLinkedList()
    c.print_list()
    c.insert_at_beginning(1)
    c.print_list()
    c.insert_at_beginning(2)
    c.print_list()
    c.insert_at_beginning(3)
    c.print_list()
    c.insert_at_end(4)
    c.insert_at_end(5)
    c.insert_at_end(6)
    c.print_list()
    c.delete_at_beginning()
    c.print_list()
    c.delete_at_end()
    c.print_list()
    c.delete_at_position(2)
    c.print_list()
    c.delete_at_position(0)
    c.print_list()
    c.delete_at_position(1)
    c.print_list()
    c.delete_at_position(2)
    c.insert_at_end(2)
    c.insert_at_end(3)
    c.insert_at_end(4)
    c.insert_at_end(5)
    c.insert_at_end(6)
    c.print_list()
    c.delete_value(4)
    c.print_list()
    c.delete_value(2)
    c.print_list()
    c.delete_value(77)


if __name__ == '__main__':
    main()
