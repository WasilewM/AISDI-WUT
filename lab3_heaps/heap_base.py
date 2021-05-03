class Heap_Base:
    def __init__(self, dimension=2):
        self.set_dimension(dimension)
        self.heap = []

    def set_dimension(self, dimension):
        if dimension >= 2:
            self._dimension = dimension
        else:
            self._dimension = 2

    def get_dimension(self):
        return self._dimension
