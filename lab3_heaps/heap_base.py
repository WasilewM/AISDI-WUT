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

    def add(self, new_value):
        if len(self.heap) <= self.next_value_index():
            self.extend_heap_list(self.next_value_index())

        self.heap[self.next_value_index()] = new_value
        self.decrement_left_per_depth()

        if self.next_value_index() == 1:
            self.set_next_value_index(
                self.next_value_index() * self.get_dimension()
            )
            self.set_left_per_depth(self.next_value_index())
            self.set_max_per_depth(self.left_per_depth())
        elif self.left_per_depth() == 0:
            self.heapify()
            self.set_next_value_index(
                (self.next_value_index() + 1 - self.max_per_depth())
                * self.get_dimension()
            )
            self.set_left_per_depth(self.next_value_index())
            self.set_max_per_depth(self.left_per_depth())
        else:
            self.heapify()
            self.set_next_value_index(self.next_value_index() + 1)

    def heapify(self):
        idx = self.next_value_index()
        while (
            self.heap[idx] > self.heap[int(idx / self.get_dimension())]
            and idx > 1
        ):
            temp = self.heap[idx]
            self.heap[idx] = self.heap[int(idx / self.get_dimension())]
            self.heap[int(idx / self.get_dimension())] = temp
            idx = idx // self.get_dimension()
