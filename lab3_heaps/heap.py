class Heap:
    def __init__(self, dimension=2):
        self._dimension = dimension
        self._heap = []

    def get_dimension(self):
        return self._dimension

    def get_heap(self):
        return self._heap

    def add(self, new_value):
        self._heap.append(new_value)
        p_index = self._find_parent_index(len(self._heap)-1)
        if p_index is not None:
            while self._heap[p_index] < new_value:
                nv_index = self._heap.index(new_value)
                self._heap[p_index], self._heap[nv_index] = self._heap[nv_index], self._heap[p_index]
                p_index = self._find_parent_index(p_index)
                if p_index is None:
                    break

    def pop(self):
        self._heap[0], self._heap[len(self._heap)-1] = self._heap[len(self._heap)-1], self._heap[0]
        self._heap.pop()
        self._heapify(0)

    def _find_parent_index(self, index):
        return (index - 1) // self._dimension if index > 0 else None

    def _find_children_ids(self, p_index):
        first_child_id = self._dimension * p_index + 1
        children_ids = (
            [first_child_id + i for i in range(self._dimension)] if
            len(self._heap) - first_child_id > self._dimension else
            [first_child_id + i for i in range(len(self._heap) - first_child_id)]
            )
        return children_ids

    def _heapify(self, index):
        largest = index
        children_ids = self._find_children_ids(index)
        for child_id in children_ids:
            if self._heap[child_id] > self._heap[largest]:
                largest = child_id
        if largest != index:
            self._heap[largest], self._heap[index] = self._heap[index], self._heap[largest]
            self._heapify(largest)

    def print(self):
        print('0: ', end='')
        height = 1
        items_per_lvl = self._dimension ** (height - 1)
        for i in range(len(self._heap)):
            if self._find_parent_index(i) is not None:
                print(f'({self._heap[i]}, came from: {self._heap[self._find_parent_index(i)]}), ', end='')
                items_per_lvl -= 1
            else:
                print(f'({self._heap[i]}, root), ', end='')
                items_per_lvl -= 1
            if items_per_lvl == 0:
                print('')
                print(f'{height}: ', end='')
                height += 1
                items_per_lvl = self._dimension ** (height - 1)
        print('')
