class Heap_Base:
    def __init__(self, dimension=2):
        self.set_dimension(dimension)
        self.heap = []
        self.set_last()

    def set_dimension(self, dimension):
        if dimension >= 2:
            self._dimension = dimension
        else:
            self._dimension = 2

    def get_dimension(self):
        return self._dimension

    def set_last(self, new_last=0):
        if new_last >= 0:
            self._last = new_last
        else:
            self._last = 0

    def last(self):
        return self._last
