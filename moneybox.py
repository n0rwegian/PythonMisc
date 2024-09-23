class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val = 0

    def can_add(self, v):
        return self.val + v <= self.capacity

    def add(self, v):
        self.val += v
