class Node:
    def __init__(self, number, company, name):
        self.number = number
        self.company = company
        self.name = name
        self.next = None

    @classmethod
    def from_string(cls, line: str):
        lines = line.split(',')
        return Node(int(lines[0]), lines[1], lines[2])

    def __str__(self):
        return f'{self.number},{self.company},{self.name}'

