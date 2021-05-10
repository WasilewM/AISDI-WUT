from heap_base import Heap_Base


class Quaternary_Heap(Heap_Base):
    def __init__(self):
        super().__init__(4)

    def delete_root(self):
        self.set_left_per_depth(self.left_per_depth() + 1)
        if self.left_per_depth() <= self.max_per_depth():
            self.set_next_value_index(self.next_value_index() - 1)
        else:
            self.set_max_per_depth(
                self.left_per_depth() / self.get_dimension()
            )
            self.set_left_per_depth(self.max_per_depth())
            self.set_next_value_index(
                self.next_value_index() / self.get_dimension()
                + self.max_per_depth() - 1
            )
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
