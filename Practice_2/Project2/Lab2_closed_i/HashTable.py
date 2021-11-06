from .FileWorking import fw

class HashTable:
    def __init__(self):
        self.size = 2
        self.fill = 0
        fw.set_lines_count(self.size)

    def hash(self, x):
        return x % self.size

    def add(self, key: int, name: str, address: str):
        h = self.hash(key)
        i = 1
        line = fw.get_line(h)
        while line != '':
            h = (h + i) % self.size
            i += 1
            line = fw.get_line(h)
        fw.set_line(h, f'{key},{name},{address}')
        self.fill += 1
        if self.fill * 2 >= self.size:
            self.rehash()

    def rehash(self):
        self.size *= 2
        self.fill = 0
        fw.swap_files()
        fw.set_lines_count(self.size)
        for line in fw.iterate_throw_old():
            key, name, address = line.split(',')
            self.add(int(key), name, address)

    def get(self, key: int):
        h = self.hash(key)
        line = fw.get_line(h)
        i = 1
        while True:
            line = line.split(',')
            if len(line) == 1:
                return None
            elif int(line[0]) == key:
                return line[1], line[2]
            else:
                h = (h + i) % self.size
                i += 1
                line = fw.get_line(h)

    def delete(self, key: int):
        h = self.hash(key)
        line = fw.get_line(h)
        i = 1
        while True:
            line = line.split(',')
            if len(line) == 1:
                return None
            elif int(line[0]) == key:
                fw.set_line(h, '')
                return None
            else:
                h = (h + i) % self.size
                i += 1
                line = fw.get_line(h)

    def print(self):
        print('-------')
        print(''.join(fw.get_all_lines()), end='')
        print('-------')