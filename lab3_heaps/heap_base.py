class Heap_Base:
    def __init__(self, dimension=2):
        self.set_dimension(dimension)
        self.heap = []
        self.set_next_value_index()
        self.set_left_per_depth()
        self.set_max_per_depth()

    def set_dimension(self, dimension):
        if dimension >= 2:
            self._dimension = dimension
        else:
            self._dimension = 2

    def get_dimension(self):
        return self._dimension

    def extend_heap_list(self, new_length):
        while len(self.heap) <= new_length:
            self.heap.append(-1)

    def set_next_value_index(self, new_next=1):
        # if new_next >= len(self.heap):
        self._next_idx = new_next

    def next_value_index(self):
        return self._next_idx

    def set_left_per_depth(self, quantity=1):
        self._left_per_depth = quantity

    def decrement_left_per_depth(self):
        self.set_left_per_depth(
            self.left_per_depth() - 1
        )

    def left_per_depth(self):
        return self._left_per_depth

    def set_max_per_depth(self, quantity=1):
        self._max_per_depth = quantity

    def max_per_depth(self):
        return self._max_per_depth
