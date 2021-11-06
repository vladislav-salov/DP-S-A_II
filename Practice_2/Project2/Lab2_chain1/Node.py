class Node:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.next = None

    @classmethod
    def from_string(cls, line: str):
        lines = line.split(',')
        return Node(int(lines[0]), lines[1])

    def __str__(self):
        return f'{self.number},{self.name}'

