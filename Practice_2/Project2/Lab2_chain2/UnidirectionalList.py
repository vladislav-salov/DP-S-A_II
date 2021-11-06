from .Node import Node

class UnidirectionalList:
    def __init__(self, line: str):
        self.len = 0
        self.start = None
        if line != '' and line != '\n':
            lines = line.split(';')
            for node_line in lines:
                self.add(Node.from_string(node_line))

    def __str__(self):
        current_node = self.start
        res = []
        while current_node is not None:
            res.append(str(current_node))
            current_node = current_node.next
        res = ';'.join(res[::-1]).replace('\n', '')
        return res

    def add(self, node: Node):
        old_start = self.start
        self.start = node
        node.next = old_start
        self.len += 1
        return self.len

    def remove(self, key: int):
        if self.start is not None:
            if self.start.number == key:
                self.start = self.start.next
            else:
                current_node = self.start
                while current_node.next is not None:
                    if current_node.next.number == key:
                        current_node.next = current_node.next.next
                    else:
                        current_node = current_node.next

    def get(self, key: int):
        current_node = self.start
        while current_node is not None:
            if current_node.number == key:
                return current_node
            current_node = current_node.next



