from heap import Heap

bheap = Heap(2)
theap = Heap(3)
qheap = Heap(4)

nums = [11, 23, 56, 99, 1, 45, 6, 8, 12, 100, 5, 1002]

for num in nums:
    bheap.add(num)
    theap.add(num)
    qheap.add(num)

print('-'*10)
print('BINARY HEAP')
bheap.print()
print('-'*10)
print('TRENARYHEAP')
theap.print()
print('-'*10)
print('QUATRENARY HEAP')
qheap.print()
print('-'*10)
