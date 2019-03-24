class PrioQureueErroe(ValueError):
    pass


class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQureueErroe("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQureueErroe("in pop")
        return self._elems.pop()
