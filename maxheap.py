class MaxHeap(object):

    def __init__(self, data=None):
        self._data = data if data else []
        self._count = len(self._data)
        self._heapify()

    def __len__(self):
        return self._count

    def __repr__(self):
        return str(self._data[:self._count])

    def add(self, item):
        if self._count < len(self._data):
            self._data[self._count] = item
        else:
            self._data.append(item)
        self._count += 1
        self._shift_up(self._count - 1)

    def pop(self):
        r = self._data[0]
        self._data[0] = self._data[self._count - 1]
        self._count -= 1
        self._shift_down(0)
        return r

    def _shift_up(self, index):
        father = (index - 1) // 2
        while father >= 0 and self._data[father] < self._data[index]:
            self._data[index], self._data[father] = self._data[father], self._data[index]
            index = father
            father = (index - 1) // 2

    def _shift_down(self, index):
        while index < self._count:
            l_child, r_child = 2 * index + 1, 2 * index + 2
            if l_child >= self._count:
                return
            if r_child < self._count:
                if self._data[index] > self._data[l_child] and self._data[index] > self._data[r_child]:
                    return
                else:
                    if self._data[l_child] > self._data[r_child]:
                        self._data[l_child], self._data[index] = self._data[index], self._data[l_child]
                        index = l_child
                    else:
                        self._data[r_child], self._data[index] = self._data[index], self._data[r_child]
                        index = r_child
            else:
                if self._data[index] > self._data[l_child]:
                    return
                else:
                    self._data[l_child], self._data[index] = self._data[index], self._data[l_child]
                    index = l_child

    def _heapify(self):
        for i in range(self._count // 2 - 1, -1, -1):
            self._shift_down(i)


# test_seq = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# mh = MaxHeap(test_seq)
# print(mh)
# mh.pop()
# print(mh)
# mh.add(17)
# print(mh)
mh = MaxHeap()
mh.add(1)
mh.add(-1)
mh.add(3)
mh.add(1)
print(mh)
