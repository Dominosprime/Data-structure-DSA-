class TreeNode:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert_recursive(root.left, val)
        elif val > root.val:
            root.right = self._insert_recursive(root.right, val)
        return root

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self._search_recursive(root.left, val)
        else:
            return self._search_recursive(root.right, val)

    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, root, val):
        if root is None:
            return root

        if val < root.val:
            root.left = self._delete_recursive(root.left, val)
        elif val > root.val:
            root.right = self._delete_recursive(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.val = self._find_min(root.right)
            root.right = self._delete_recursive(root.right, root.val)

        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

class MinHeap:
    def _init_(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def delete_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest_index = right_child_index

        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._heapify_down(smallest_index)

class PriorityQueue:
    def _init_(self):
        self.heap = MinHeap()

    def enqueue(self, val):
        self.heap.insert(val)

    def dequeue(self):
        return self.heap.delete_min()

# Assignment

def is_valid_bst(root):
    def _is_valid_bst_recursive(node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (_is_valid_bst_recursive(node.left, min_val, node.val) and
                _is_valid_bst_recursive(node.right, node.val, max_val))

    return _is_valid_bst_recursive(root, float('-inf'), float('inf'))

def print_bst_sorted(root):
    def _inorder_traversal(node):
        if node:
            _inorder_traversal(node.left)
            print(node.val, end=" ")
            _inorder_traversal(node.right)
    _inorder_traversal(root)
    print()

def build_max_heap(arr):
    def _max_heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _max_heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _max_heapify(arr, n, i)
    return arr

def get_top_k(arr, k):
    max_heap = build_max_heap(arr)
    return max_heap[:k]

# Example Usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("BST Min:", bst.find_min())
print("BST Max:", bst.find_max())
print("Search 4:", bst.search(4))
print("Search 9:", bst.search(9))

root = bst.root
print("Is BST valid:", is_valid_bst(root))
print("BST Sorted:", end=" ")
print_bst_sorted(root)

pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(4)
pq.enqueue(2)
print("Priority Queue Dequeue:", pq.dequeue())
print("Priority Queue Dequeue:", pq.dequeue())

unsorted_arr = [12, 11, 13, 5, 6, 7]
top_3 = get_top_k(unsorted_arr, 3)
print("Top 3:", top_3)