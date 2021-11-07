class Combining:
    def __init__(self, combining, file_handler):
        self.combining = combining
        self.file_handler = file_handler

    def get(self, key) -> str:
        from time import perf_counter
        a = perf_counter()
        n = self.combining.get(key)
        b = perf_counter()
        print(f"Затраченное время на получение записи: {b - a:0.7f} с.")
        if n != -1:
            return self.file_handler.get(n)
        else:
            return 'None'

    def add(self, key, **kwargs) -> None:
        value = self.file_handler.add(key=key, **kwargs)
        self.combining.add(key, value)

    def remove(self, key) -> None:
        value = self.combining.get(key)
        self.combining.remove(key)
        self.file_handler.remove(value)
