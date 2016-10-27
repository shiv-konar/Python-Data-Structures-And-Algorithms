from Nodes import SingleLinkedListNode


class Stack:
    """ Constructor to initialize the stack """
    def __init__(self, size_of_stack=99999):
        self.head = None
        self.length = 0
        self.max_size = size_of_stack

    """ Internal method to push element on to the stack """
    def __insert_at_beginning(self, data):
        new_node = SingleLinkedListNode()
        new_node.set_data(data)

        if self.length > self.max_size - 1:
            print "Stack is full"
            return
        else:
            if self.length == 0:
                self.head = new_node
            else:
                new_node.set_next(self.head)
                self.head = new_node
            self.length += 1

    """ Internal method to pop element from the stack """
    def __delete_at_beginning(self):
        return_val = None
        if self.length == 0:
            print "Stack is empty"
            return return_val
        else:
            return_val = self.head.get_data()
            print "Value {0} popped".format(return_val)
            self.head = self.head.get_next()
            self.length -= 1
            return return_val

    """ Method to PUSH element on to the stack """
    def push(self, data):
        self.__insert_at_beginning(data)

    """ Method to POP element from the stack """
    def pop(self):
        self.__delete_at_beginning()

    """ Method to return the top most element on the stack, without removing the item """
    def peek(self):
        top = self.head.get_data()
        print "Top Element: " + str(top)
        return top

    """ Method to print the elements on the stack """
    def print_stack(self):
        if self.length == 0:
            print "Stack is empty"
        else:
            current = self.head
            while current.has_next():
                print str(current.get_data()) + " ---> ",
                current = current.get_next()
            print str(current.get_data())

    """ Method to check if the stack is full """
    def is_stack_full(self):
        stack_full = self.length >= self.max_size
        print "Is stack full - " + str(stack_full)
        return stack_full

    """ Method to check if stack has space left in to push elements """
    def is_stack_empty(self):
        stack_empty = self.length < self.max_size
        print "Is stack empty - " + str(stack_empty)
        return stack_empty

    """ Method to check the size of the stack """
    def stack_size(self):
        print "Stack size: " + str(self.length)
        return self.length


def main():
    s = Stack()
    s.is_stack_empty()
    s.is_stack_full()
    s.print_stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.print_stack()

    s.peek()
    s.stack_size()

    s.pop()
    s.print_stack()

    s.pop()
    s.print_stack()

    print "------------------------"

    s1 = Stack(3)
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.push(40)
    s1.print_stack()
    s1.push(50)
    s1.print_stack()
    s1.is_stack_empty()
    s1.is_stack_full()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.is_stack_empty()
    s1.is_stack_full()


if __name__ == '__main__':
    main()
