class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.oldestItem = 0

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            if self.oldestItem < self.capacity:
                self.items[self.oldestItem] = item
                self.oldestItem += 1
            else:
                self.items[0] = item

    def get(self):
        return [value for value in self.items if value is not None]
