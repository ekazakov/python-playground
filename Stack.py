class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[(len(self.items) - 1)]

    def size(self):
        return len(self.items)


def mathces(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def is_balanced(string):
    stack = Stack()

    for ch in string:
        if ch in '({[':
            stack.push(ch)
        elif stack.isEmpty():
            return False
        else:
            top = stack.pop()
            if not mathces(top, ch):
                return False

    return stack.isEmpty()


def base_converter(num, base):
    digits = "0123456789ABCDEF"
    stack = Stack()

    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    new_string = ''
    while not stack.isEmpty():
        new_string += digits[stack.pop()]

    return new_string

