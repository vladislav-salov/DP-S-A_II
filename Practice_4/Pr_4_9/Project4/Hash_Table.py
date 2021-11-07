from HT_F_Working import fw
compares = 0


class HT:
    def __init__(self):
        self.size = 2
        fw.set_lines_count(2)

    def hash(self, x: int):
        return x % self.size

    def add(self, key: str, value: str):
        key = int(key)
        node = NodeOfHT(key, value)
        h = self.hash(node.key)
        ul = UnidirectionalList(fw.get_line(h))
        count = ul.add(node)
        fw.set_line(h, str(ul))
        if count > self.size * 0.75:
            self.rehash()

    def remove(self, key):
        key = int(key)
        h = self.hash(key)
        ul = UnidirectionalList(fw.get_line(h))
        ul.remove(key)
        fw.set_line(h, str(ul))

    def get(self, key):
        global compares
        compares = 0
        key = int(key)
        h = self.hash(key)
        ul = UnidirectionalList(fw.get_line(h))
        if str(ul.get(key)).replace('\n', '') == 'None':
            return -1
        else:
            return list(map(int, str(ul.get(key)).replace('\n', '').split(',')))[1]

    def rehash(self):
        fw.swap_files()
        self.size *= 2
        fw.set_lines_count(self.size)
        for node_line in fw.iterate_throw_old_nodes():
            self.__add_node(NodeOfHT.from_string(node_line))

    def fill_from_file(self, file_path):
        file = open(file_path, 'r')
        for line in file:
            line = line.replace('\n', '')
            if line != '':
                self.__add_node(NodeOfHT.from_string(line))

    @staticmethod
    def print():
        print('-------')
        print(''.join(fw.get_all_lines()), end='')
        print('-------')

    def __add_node(self, node):
        self.add(node.key, node.value)


class NodeOfHT:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.key},{self.value}'

    @classmethod
    def from_string(cls, line: str):
        lines = line.split(',')
        return NodeOfHT(int(lines[0]), lines[1])


class UnidirectionalList:
    def __init__(self, line: str):
        self.len = 0
        self.start = None
        if line != '' and line != '\n':
            lines = line.split(';')
            for node_line in lines:
                self.add(NodeOfHT.from_string(node_line))

    def __str__(self):
        current_node = self.start
        res = []
        while current_node is not None:
            res.append(str(current_node))
            current_node = current_node.next
        res = ';'.join(res[::-1]).replace('\n', '')
        return res

    def add(self, node: NodeOfHT):
        old_start = self.start
        self.start = node
        node.next = old_start
        self.len += 1
        return self.len

    def remove(self, key: int):
        if self.start is not None:
            if self.start.key == key:
                self.start = self.start.next
            else:
                current_node = self.start
                while current_node.next is not None:
                    if current_node.next.key == key:
                        current_node.next = current_node.next.next
                    else:
                        current_node = current_node.next

    def get(self, key: int):
        current_node = self.start
        while current_node is not None:
            global compares
            compares += 1
            if current_node.key == key:
                return current_node
            current_node = current_node.next
