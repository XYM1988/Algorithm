class ArrayStack():
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, element):
        """Add element element to the top of the Stack"""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise exception if the stack is empty"""
        if self.is_empty():
            raise IndexError
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise exception if the stack is empty"""
        if self.is_empty():
            raise IndexError
        return  self._data.pop()