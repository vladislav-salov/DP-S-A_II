class Combining:
    def __init__(self, combining, file_handler):
        self.combining = combining
        self.file_handler = file_handler

    def get(self, key) -> str:
        from time import perf_counter  # Импорт perf_counter из библиотеки time.
        a = perf_counter()  # Время до получения записи.
        n = self.combining.get(key)
        b = perf_counter()  # Время после получения записи.
        print(f"Потраченное время на получение записи: {b - a:0.7f} с.")  # Потраченное время на получение записи.
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
