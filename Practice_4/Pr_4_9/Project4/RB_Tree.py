RED = 'R'
BLACK = 'B'
compares = 0
turns = 0


class RBT:
    def __init__(self):
        self.start = None
        self.size = 0

    def __str__(self) -> str:
        if self.start is not None:
            sa = []
            self.start.add_to_line(sa, 0)
            return '\n'.join(sa)
        else:
            return 'Empty'

    def isRed(self, node):
        return node and node.color == RED

    def isBlack(self, node):
        return node is None or node.color == BLACK

    def predecessor(self, node):
        if node is None:
            return None
        if node.left:
            p = node.left
            while p.right:
                p = p.right
            return p
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def successor(self, node):
        if node is None:
            return None
        if node.right:
            s = node.right
            while s.left:
                s = s.left
            return s
        while node.parent and node is node.parent.right:
            node = node.parent
        return node.parent

    def add(self, key, value):
        if self.start is None:
            self.start = NodeOfRBT(key, value)
            self.size += 1
            self._insert(self.start)
            return
        parent = self.start
        node = self.start
        flag = 0
        while node:
            parent = node
            if key > node.key:
                node = node.right
                flag = 0
            elif key < node.key:
                node = node.left
                flag = 1
            else:
                node.key = key
                return
        new = NodeOfRBT(key=key, value=value, parent=parent)
        if flag == 0:
            parent.right = new
        else:
            parent.left = new
        self.size += 1
        self._insert(new)

    def _insert(self, node):
        parent = node.parent
        if parent is None:
            node.paint(BLACK)
            return
        if self.isBlack(parent):
            return
        grand = parent.parent
        grand.paint(RED)
        uncle = parent.sibling()
        if self.isRed(uncle):
            parent.paint(BLACK)
            uncle.paint(BLACK)
            self._insert(grand)
            return
        if parent.isLeftChild():
            if node.isLeftChild():
                parent.paint(BLACK)
            else:
                node.paint(BLACK)
                self.LeftRotate(parent)
            self.RightRotate(grand)
        else:  # Если чёрный дядя:
            if node.isLeftChild():
                node.paint(BLACK)
                self.RightRotate(parent)
            else:
                parent.paint(BLACK)
            self.LeftRotate(grand)

    def get(self, key) -> int:
        global compares
        compares = 0
        if self.start is None:
            return -1
        else:
            return self.start.get(key)

    def _search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._search(subtree.left, key)
        elif key > subtree.key:
            return self._search(subtree.right, key)
        else:
            return subtree.key

    def remove(self, key):
        node = self._search(self.start, key)
        if node is None:
            return
        self.size -= 1
        if node.left and node.right:
            s = self.successor(node)
            node.key = s.key
            node = s
        replacement = node.left if node.left else node.right
        if replacement:
            replacement.parent = node.parent
            if node.parent is None:
                self.start = replacement
            elif node.parent.left is node:
                node.parent.left = replacement
            else:
                node.parent.right = replacement
            self._remove(replacement)
            node.left = node.right = node.parent = None
        elif node.parent is None:
            self.start = None
            self._remove(node)
        else:
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self._remove(node)
            node.parent = None

    def _remove(self, node):
        if self.isRed(node):
            node.paint(BLACK)
            return
        parent = node.parent
        if parent is None:
            return
        left = node.isLeftChild() or parent.left is None
        sibling = parent.right if left else parent.left
        if left:
            if self.isRed(sibling):
                sibling.paint(BLACK)
                parent.paint(RED)
                self.LeftRotate(parent)
                sibling = parent.right
            if self.isBlack(sibling.left) and self.isBlack(sibling.right):
                parentBlack = self.isBlack(parent)
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:
                    if parent.isLeftChild():
                        self._remove(parent)
            else:
                if sibling.right.isBlack():
                    self.RightRotate(sibling)
                    sibling = parent.right
                    sibling.color = parent.color
                    parent.paint(BLACK)
                    sibling.right.paint(BLACK)
                    self.LeftRotate(parent)
        else:
            if self.isRed(sibling):
                sibling.paint(BLACK)
                parent.paint(RED)
                self.RightRotate(parent)
                sibling = parent.left
            if self.isBlack(sibling.left) and self.isBlack(sibling.right):
                parentBlack = parent.isBlack()
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:
                    if parent.isLeftChild():
                        self._remove(parent)
            else:
                if self.isBlack(sibling.left):
                    self.LeftRotate(sibling)
                    sibling = parent.left
                sibling.color = parent.color
                parent.paint(BLACK)
                sibling.left.color = BLACK
                self.RightRotate(parent)

    def LeftRotate(self, grand):
        global turns
        turns += 1
        parent = grand.right
        child = parent.left
        grand.right = child
        parent.left = grand
        self._rotate(grand, parent, child)

    def RightRotate(self, grand):
        global turns
        turns += 1
        parent = grand.left
        child = parent.right
        grand.left = child
        parent.right = grand
        self._rotate(grand, parent, child)

    def _rotate(self, grand, parent, child):
        if grand.isLeftChild():
            grand.parent.left = parent
        elif grand.isRightChild():
            grand.parent.right = parent
        else:
            self.start = parent
        if child:
            child.parent = grand
        parent.parent = grand.parent
        grand.parent = parent


class NodeOfRBT:
    def __init__(self, key=None, value=1, parent=None, color=RED):
        self.key = key
        self.value = value
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

    def paint(self, color):
        self.color = color

    def isLeftChild(self):
        return self.parent and self is self.parent.left

    def isRightChild(self):
        return self.parent and self is self.parent.right

    def sibling(self):
        if self.isLeftChild():
            return self.parent.right
        if self.isRightChild():
            return self.parent.left
        return None

    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()

    def add(self, key=None, value=1, parent=None, color=RED) -> None:
        if key > self.key:
            if self.right is None:
                self.right = NodeOfRBT(key, value, parent, color)
            else:
                self.right.add(key, value, parent, color)
        elif key == self.key:
            self.value += value
        else:
            if self.left is None:
                self.left = NodeOfRBT(key, value, parent, color)
            else:
                self.left.add(key, value, parent, color)

    def add_to_line(self, sa, depth) -> None:
        if self.right is not None:
            self.right.add_to_line(sa, depth + 1)
        sa.append('         ' * depth + f'[{self.color}]<{self.key}:{self.value}>({depth})')
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
