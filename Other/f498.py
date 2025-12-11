def main():
    from sys import stdin
    e = stdin.readline
    content = []

    class HeapNode:
        def __init__(self): self.heap = []

        def get_parent_index(self, i): return (i - 1) // 2

        def swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        def insert(self, value):
            self.heap.append(value)
            self._bubble_up(len(self.heap) - 1)

        def _bubble_up(self, index):
            raise NotImplementedError("not define")
    
    class MaxHeap(HeapNode):
        def _bubble_up(self, index):
            while True:
                p_index = self.get_parent_index(index)
                if self.heap[index] > self.heap[p_index]:
                    self.swap(index, p_index)
                    index = p_index
                else: break
                if index <= 0: break

    class MinHeap(HeapNode):
        def _bubble_up(self, index):
            while True:
                p_index = self.get_parent_index(index)
                if self.heap[index] < self.heap[p_index]:
                    self.swap(index, p_index)
                    index = p_index
                else: break
                if index <= 0: break
    
    while True:
        if not e(): break
        d = list(map(int, e().split()))
        h = MinHeap()
        for i in d: h.insert(i)
        content.append(" ".join(map(str, h.heap)))
        h = MaxHeap()
        for i in d: h.insert(i)
        content.append(" ".join(map(str, h.heap)))
    
    print("\n".join(content))
main()