class OrderedStream(object):

    def __init__(self, n):
        self.stream = [""] * (n + 1)   # 1-indexed
        self.ptr = 1

    def insert(self, idKey, value):
        self.stream[idKey] = value
        res = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] != "":
            res.append(self.stream[self.ptr])
            self.ptr += 1

        return res