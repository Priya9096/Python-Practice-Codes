class Counter:
    def __init__(self,limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self.count < self.limit:
            self.count = self.count + 1
            return self.count
        else:
            raise StopIteration

c = Counter(5)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
