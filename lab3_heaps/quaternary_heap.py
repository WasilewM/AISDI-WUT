from heap_base import Heap_Base


class Quaternary_Heap(Heap_Base):
    def __init__(self):
        super().__init__(4)

    def add(self, new_value):
        if len(self.heap) <= self.next_value_index():
            self.extend_heap_list(self.next_value_index())

        self.heap[self.next_value_index()] = new_value
        # self.increment_last()

        if self.next_value_index() == 1:
            self.set_next_value_index(self.next_value_index() * 4)
        else:
            self.heapify()
            self.set_next_value_index(self.next_value_index() + 1)

    def heapify(self):
        idx = self.next_value_index()
        while self.heap[idx] > self.heap[int(idx / 4)]:
            temp = self.heap[idx]
            self.heap[idx] = self.heap[int(idx / 4)]
            self.heap[int(idx / 4)] = temp

            idx = idx // 4
            if self.heap[int(idx / 4)] is None:
                break
