from heap_base import Heap_Base


class Quaternary_Heap(Heap_Base):
    def __init__(self):
        super().__init__(4)

    def add(self, new_value):
        if len(self.heap) <= self.next_value_index():
            self.extend_heap_list(self.next_value_index())

        self.heap[self.next_value_index()] = new_value
        self.decrement_left_per_depth()

        if self.next_value_index() == 1:
            self.set_next_value_index(self.next_value_index() * 4)
            self.set_left_per_depth(self.next_value_index())
            self.set_max_per_depth(self.left_per_depth())
        elif self.left_per_depth() == 0:
            self.heapify()
            self.set_next_value_index(
                (self.next_value_index() + 1 - self.max_per_depth()) * 4
            )
            self.set_left_per_depth(self.next_value_index())
            self.set_max_per_depth(self.left_per_depth())
        else:
            self.heapify()
            self.set_next_value_index(self.next_value_index() + 1)

    def heapify(self):
        idx = self.next_value_index()
        while self.heap[idx] > self.heap[int(idx / 4)] and idx > 1:
            temp = self.heap[idx]
            self.heap[idx] = self.heap[int(idx / 4)]
            self.heap[int(idx / 4)] = temp
            idx = idx // 4

    def delete_root(self):
        self.set_next_value_index(self.next_value_index() - 1)
        self.heap[1] = self.heap[self.next_value_index()]
        self.heap = self.heap[:self.next_value_index()]

        self.restore()

    def restore(self):
        buffer = 1
        while buffer < len(self.heap):
            buffer *= 4
        self.extend_heap_list(len(self.heap) + buffer)

        idx = 1
        while (
            self.heap[idx] < self.heap[4 * idx] or
            self.heap[idx] < self.heap[4 * idx + 1] or
            self.heap[idx] < self.heap[4 * idx + 2] or
            self.heap[idx] < self.heap[4 * idx + 3]
        ):
            max_son_value = max(
                self.heap[4 * idx],
                self.heap[4 * idx + 1],
                self.heap[4 * idx + 2],
                self.heap[4 * idx + 3]
            )

            if self.heap[4 * idx] == max_son_value:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[4 * idx]
                self.heap[4 * idx] = temp

            if self.heap[4 * idx + 1] == max_son_value:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[4 * idx + 1]
                self.heap[4 * idx + 1] = temp

            if self.heap[4 * idx + 2] == max_son_value:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[4 * idx + 2]
                self.heap[4 * idx + 2] = temp

            if self.heap[4 * idx + 3] == max_son_value:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[4 * idx + 3]
                self.heap[4 * idx + 3] = temp

            idx *= 4
