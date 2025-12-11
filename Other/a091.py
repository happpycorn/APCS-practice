def main():
    from sys import stdin
    e = stdin.readline
    content = []

    class HeapNode:
        def __init__(self): self.heap = []
        def get_parent_point(self, i): return (i-1)//2
        def get_left_child(self, i): return 2 * i + 1
        def get_right_child(self, i): return 2 * i + 2
        def swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        def insert(self, value):
            self.heap.append(value)
            self._bubble_up(len(self.heap)-1)
        def _bubble_up(self, idx): pass
        def pop(self):
            if not self.heap: return None
            
            root_val = self.heap[0]
            last_val = self.heap.pop()
            
            if self.heap:
                self.heap[0] = last_val
                self._sink_down(0)
            
            return root_val
        def _sink_down(self, idx): pass
    
    class MaxHeap(HeapNode):
        def _bubble_up(self, idx):
            while True:
                p_idx = self.get_parent_point(idx)
                if self.heap[idx] > self.heap[p_idx]:
                    self.swap(idx, p_idx)
                    idx = p_idx
                else: break
                if idx <= 0: break

        def _sink_down(self, idx):
            n = len(self.heap)
            
            while True:
                left = self.get_left_child(idx)
                right = self.get_right_child(idx)
                smallest = idx

                if left < n and self.heap[left] > self.heap[smallest]: smallest = left
                
                if right < n and self.heap[right] > self.heap[smallest]: smallest = right
                
                if smallest != idx:
                    self.swap(idx, smallest)
                    idx = smallest
                else: break

    class MinHeap(HeapNode):
        def _bubble_up(self, idx):
            while True:
                p_idx = self.get_parent_point(idx)
                if self.heap[idx] < self.heap[p_idx]:
                    self.swap(idx, p_idx)
                    idx = p_idx
                else: break
                if idx <= 0: break

        def _sink_down(self, idx):
            n = len(self.heap)
            
            while True:
                left = self.get_left_child(idx)
                right = self.get_right_child(idx)
                smallest = idx

                if left < n and self.heap[left] < self.heap[smallest]: smallest = left
                
                if right < n and self.heap[right] < self.heap[smallest]: smallest = right
                
                if smallest != idx:
                    self.swap(idx, smallest)
                    idx = smallest
                else: break
    
    maxh = MaxHeap()
    minh = MinHeap()
    del_map = {}

    while True:
        a = e()
        if not a: break
        d = list(map(int, a.split()))
        if d[0] == 1:
            maxh.insert(d[1])
            minh.insert(d[1])
            if d[1] in del_map: del_map[d[1]] += 1
            else: del_map[d[1]] = 1
        if d[0] == 2:
            while True:
                a = maxh.pop()
                if a is None: break
                if del_map[a] > 0:
                    del_map[a] -= 1
                    break
            content.append(a)
        if d[0] == 3:
            while True:
                a = minh.pop()
                if a is None: break
                if del_map[a] > 0:
                    del_map[a] -= 1
                    break
            content.append(a)
    print("\n".join(map(str, content)))
            
main()