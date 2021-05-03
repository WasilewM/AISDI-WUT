class Heap_Base:
    def __init__(self, dimension=2):
        self.set_dimension(dimension)
        self.heap = []
        # self.set_last()
        self.set_next_value_index()

    def set_dimension(self, dimension):
        if dimension >= 2:
            self._dimension = dimension
        else:
            self._dimension = 2

    def get_dimension(self):
        return self._dimension

    # def set_last(self, new_last=0):
    #     if new_last >= 0:
    #         self._last = new_last
    #     else:
    #         self._last = 0

    # def last(self):
    #     return self._last

    # def increment_last(self):
    #     self.set_last(self.last() + 1)

    def extend_heap_list(self, new_length):
        while len(self.heap) <= new_length:
            self.heap.append(None)

    def set_next_value_index(self, new_next=1):
        if new_next >= len(self.heap):
            self._next_idx = new_next

    def next_value_index(self):
        return self._next_idx
