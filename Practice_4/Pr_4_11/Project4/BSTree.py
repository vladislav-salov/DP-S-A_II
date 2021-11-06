compares = 0


class BSTree:
    def __init__(self):
        self.start = None

    def add(self, key, value) -> None:
        if self.start is None:
            self.start = Node(key, value)
        else:
            self.start.add(key, value)

    def __str__(self) -> str:
        if self.start is not None:
            sa = []
            self.start.add_to_line(sa, 0)
            return '\n'.join(sa)
        else:
            return 'Empty'

    def remove(self, key) -> None:
        if self.start is not None:
            self.start = self.start.remove(key)

    def get(self, key) -> int:
        global compares
        compares = 0
        if self.start is None:
            return -1
        else:
            return self.start.get(key)


class Node:
    def __init__(self, key, value=1):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def add(self, key, value=1) -> None:
        if key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.add(key, value)
        elif key == self.key:
            self.value += value
        else:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.add(key, value)

    def add_to_line(self, sa, depth) -> None:
        if self.right is not None:
            self.right.add_to_line(sa, depth + 1)
        sa.append('         ' * depth + f'{self.key}|{self.value}')
        if self.left is not None:
            self.left.add_to_line(sa, depth + 1)

    def remove(self, key):
        if key > self.key:
            if self.right is not None:
                self.right = self.right.remove(key)
            return self
        elif key < self.key:
            if self.left is not None:
                self.left = self.left.remove(key)
            return self
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                self.key, self.value = self.left.find_max()
                self.left = self.left.remove(self.key)
                return self

    def find_max(self) -> (str, int):
        if self.right is None:
            return self.key, self.value
        else:
            return self.right.find_max()

    def get(self, key):
        global compares
        compares += 1
        if self.key == key:
            return self.value
        if key > self.key and self.right is not None:
            return self.right.get(key)
        if key < self.key and self.left is not None:
            return self.left.get(key)
        return -1
