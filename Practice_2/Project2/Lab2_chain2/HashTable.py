from .UnidirectionalList import UnidirectionalList, Node
from .FileWorking import fw

class HashTable:
    def __init__(self):
        self.size = 2
        fw.set_lines_count(2)

    def hash(self, x: int):
        return x % self.size

    def add(self, number: int, company: str, name: str):
        node = Node(number, company, name)
        h = self.hash(node.number)
        ul = UnidirectionalList(fw.get_line(h))
        count = ul.add(node)
        fw.set_line(h, str(ul))
        if count > self.size * 0.75:
            self.rehash()

    def remove(self, number):
        h = self.hash(number)
        ul = UnidirectionalList(fw.get_line(h))
        ul.remove(number)
        fw.set_line(h, str(ul))

    def get(self, number):
        h = self.hash(number)
        ul = UnidirectionalList(fw.get_line(h))
        return str(ul.get(number)).replace('\n', '')

    def rehash(self):
        fw.swap_files()
        self.size *= 2
        fw.set_lines_count(self.size)
        for node_line in fw.iterate_throw_old_nodes():
            self.__add_node(Node.from_string(node_line))

    def fill_from_file(self, file_path):
        file = open(file_path, 'r')
        for line in file:
            line = line.replace('\n', '')
            if line != '':
                self.__add_node(Node.from_string(line))

    def print(self):
        print('-------')
        print(''.join(fw.get_all_lines()), end='')
        print('-------')

    def __add_node(self, node: Node):
        self.add(node.number, node.company, node.name)