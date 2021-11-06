RED = 'КРАСНЫЙ'
BLACK = 'ЧЁРНЫЙ'
compares = 0
turns = 0


class RBNode:
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
        # Имеет родительский узел и является левым потомком.
        return self.parent and self is self.parent.left

    def isRightChild(self):
        # Имеет родительский узел и является правильным потомком.
        return self.parent and self is self.parent.right

    def sibling(self):
        if self.isLeftChild():  # Если это левый дочерний элемент, то вернуться к правому дочернему элементу.
            return self.parent.right
        if self.isRightChild():  # Если это правый дочерний элемент, то вернуться к левому дочернему элементу.
            return self.parent.left
        return None  # Ни левый, ни правый – отсутствие дочернего узла.

    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()

    def add(self, key=None, value=1, parent=None, color=RED) -> None:
        if key > self.key:
            if self.right is None:
                self.right = RBNode(key, value, parent, color)
            else:
                self.right.add(key, value, parent, color)
        elif key == self.key:
            self.value += value
        else:
            if self.left is None:
                self.left = RBNode(key, value, parent, color)
            else:
                self.left.add(key, value, parent, color)

    def add_to_line(self, sa, depth) -> None:
        if self.right is not None:
            self.right.add_to_line(sa, depth + 1)
        sa.append('         ' * depth + f'–{self.color}–{self.key}|{self.value}')
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


class RBTree:
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
        # Текущий узел существует и красный.
        return node and node.color == RED

    def isBlack(self, node):
        # Текущий узел не существует (внешний узел - чёрный по умолчанию) или цвет чёрный.
        return node is None or node.color == BLACK

    def predecessor(self, node):
        if node is None:
            return None
        if node.left:  # Самый большой узел левого поддерева - предшественник.
            p = node.left
            while p.right:
                p = p.right
            return p
        # Нет левого поддерева => если это правое поддерево родительского - родительский является предшественником.
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def successor(self, node):
        if node is None:
            return None
        if node.right:  # Наименьший узел правого поддерева является преемником.
            s = node.right
            while s.left:
                s = s.left
            return s
        # Правого поддерева нет => если это левое поддерево родительского - родительский является преемником.
        while node.parent and node is node.parent.right:
            node = node.parent
        return node.parent

    def add(self, key, value):
        if self.start is None:
            self.start = RBNode(key, value)
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
        new = RBNode(key=key, value=value, parent=parent)
        if flag == 0:
            parent.right = new
        else:
            parent.left = new
        self.size += 1
        self._insert(new)

    def _insert(self, node):
        parent = node.parent
        # Добавить корневой узел или переполнить корневой узел.
        if parent is None:
            node.paint(BLACK)
            return
        # Чёрный родительский узел => вставить напрямую без обработки.
        if self.isBlack(parent):
            return
        # Случай, когда родительский узел - красный.
        grand = parent.parent
        grand.paint(RED)  # Дед всегда будет красным, независимо от цвета дяди.
        uncle = parent.sibling()
        # Переполнение узла.
        if self.isRed(uncle):  # Если красный дядя:
            parent.paint(BLACK)
            uncle.paint(BLACK)
            self._insert(grand)  # Узел переполняется, дед - как вновь вставленный узел.
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
        # Фактически, удаленный узел - это конечный узел (т.е. последний уровень B-дерева).
        node = self._search(self.start, key)
        if node is None:
            return
        self.size -= 1
        if node.left and node.right:  # Узел со степенью 2: нахождение его преемника.
            s = self.successor(node)
            node.key = s.key
            node = s
        replacement = node.left if node.left else node.right  # Элемент, используемый для замены.
        if replacement:  # Узел степени 1.
            replacement.parent = node.parent
            if node.parent is None:  # Корневой узел.
                self.start = replacement
            elif node.parent.left is node:  # Левое поддерево родительского узла.
                node.parent.left = replacement
            else:  # Правое поддерево родительского узла.
                node.parent.right = replacement
            self._remove(replacement)
            node.left = node.right = node.parent = None
        elif node.parent is None:  # Корневой узел.
            self.start = None
            self._remove(node)
        else:  # Листовой узел.
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self._remove(node)
            node.parent = None

    def _remove(self, node):
        if self.isRed(node):  # Если заменяемый узел - красный, то покрасить его в чёрный.
            node.paint(BLACK)
            return
        parent = node.parent
        if parent is None:
            return
        # Альтернативный узел - чёрный.
        left = node.isLeftChild() or parent.left is None
        sibling = parent.right if left else parent.left
        if left:  # Родственный узел - справа.
            if self.isRed(sibling):  # Если красный брат:
                sibling.paint(BLACK)
                parent.paint(RED)
                self.LeftRotate(parent)
                sibling = parent.right
            if self.isBlack(sibling.left) and self.isBlack(sibling.right):
                parentBlack = self.isBlack(parent)
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:  # Если родительский элемент также чёрный, то это вызовет потерю родительского значения.
                    if parent.isLeftChild():
                        self._remove(parent)  # Рассматривать родителя как удалённый узел.
            else:  # У родственного узла есть хотя бы один красный узел.
                if sibling.right.isBlack():
                    self.RightRotate(sibling)
                    sibling = parent.right
                    sibling.color = parent.color
                    parent.paint(BLACK)
                    sibling.right.paint(BLACK)
                    self.LeftRotate(parent)
        else:  # Родственный узел слева, полностью симметричен верхней стороне.
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
        # Сохранение соответствующего отношения наведения после поворота.
        if grand.isLeftChild():
            grand.parent.left = parent
        elif grand.isRightChild():
            grand.parent.right = parent
        else:
            self.start = parent
        if child:  # Указание родительского элемента ребёнка на деда.
            child.parent = grand
        parent.parent = grand.parent  # Направление родительского элемента на главного родителя.
        grand.parent = parent

    '''def preOrder(self, subtree):
        if subtree is not None:
            print("%d" % subtree.key, end=' ')
            self.preOrder(subtree.left)
            self.preOrder(subtree.right)


if __name__=='__main__':
    rb = RBTree()
    a = [61, 2, 58, 74, 97, 44, 68, 20, 90, 28, 18, 22, 77, 78, 51]
    for x in a:
        rb.insert(x)
    rb.preOrder(rb.start) # 58 20 2 18 28 22 44 51 74 61 68 90 77 78 97
    print()
    rb.remove(97)
    rb.preOrder(rb.start) # 58 20 2 18 28 22 44 51 74 61 68 78 77 90
    print()
    rb.remove(28)
    rb.preOrder(rb.start) # 58 20 2 18 44 22 51 74 61 68 78 77 90
    print()
    rb.remove(74)
    rb.preOrder(rb.start) # 58 20 2 18 44 22 51 77 61 68 78 90
    print()
    from time import perf_counter
    a = perf_counter()
    print(rb._search(rb.start, 68))
    b = perf_counter()
    print(f"Поиск узла занял {b - a:0.7f} секунд.")
    rb._search(rb.start, 68)'''
