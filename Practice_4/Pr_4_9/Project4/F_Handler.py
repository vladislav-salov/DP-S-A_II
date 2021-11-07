from typing import Dict


class FileHandler:
    def __init__(self, file_name: str, data: Dict[str, int]):
        self.file_name = file_name
        self.data = data
        self.size = 0
        self.length = 0
        with open(self.file_name, 'w'):
            pass

    def add(self, **kwargs) -> str:
        res = []
        for key in self.data.keys():
            s = str(kwargs[key]).ljust(self.data[key], ' ')
            res.append(s)
        res = ''.join(map(str, res))
        with open(self.file_name, 'ab') as f:
            f.write(res.encode())
            self.length = len(res.encode())
        self.size += 1
        return self.size - 1

    def get(self, n: int) -> str:
        pos = self.length * n
        with open(self.file_name, 'rb') as f:
            f.seek(pos)
            res = f.read(self.length).decode()
        return res

    def remove(self, n: int) -> None:
        pass
