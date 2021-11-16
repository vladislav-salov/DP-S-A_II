# Класс, реализующий граф и некоторые операции с ним.
class Graph:
    # Конструктор класса.
    def __init__(self, m, n):
        self.hor_vertex = n + 1  # Количество вершин поля по горизонтали.
        self.vert_vertex = m + 1  # Количество вершин поля по вертикали.
        self.vertexes = self.hor_vertex * self.vert_vertex  # Общее количество вершин поля (узлов графа).
        # Установка спика смежных вершин.
        self.adj_list = list()
        for i in range(self.vertexes):
            self.adj_list.append([])
        # Установка матрицы смежности.
        self.adj_mat = [[float('inf')] * self.vertexes for _ in range(self.vertexes)]
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat)):
                if i == j:
                    self.adj_mat[i][j] = 0

    # Вставка взвешенного ребра в граф.
    def connect(self, node1, node2, weight):
        self.adj_list[node1].append([node2, weight])  # Вставка ребра в список смежных вершин.
        self.adj_mat[node1][node2] = weight  # Вставка ребра в матрицу смежности для алгоритма перебора вершин.

    # Алгоритм перебора вершин (метод "грубой силы").
    def brute_force(self):
        from time import perf_counter  # Импорт perf_counter из библиотеки time.
        time_a = perf_counter()  # Время перед работой алгоритма.
        v = len(self.adj_mat)  # Количество узлов графа как длина матрицы смежности.
        min_dist = self.adj_mat  # Копия матрицы смежности для дальнейшего перезаполнения под матрицу кратчайших путей.
        compares = 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        for k in range(v):
            compares += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for i in range(v):
                compares += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
                for j in range(v):
                    compares += 1  # Увеличение количества сравнений на 1: перед условием if.
                    if min_dist[i][j] > min_dist[i][k] + min_dist[k][j]:
                        min_dist[i][j] = min_dist[i][k] + min_dist[k][j]  # Величина текущего кратчайшего пути из i в j.
                    compares += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
                compares += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            compares += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
        time_b = perf_counter()  # Время после работы алгоритма.
        print(f"Затраченное время на работу алгоритма: {time_b - time_a:0.7f} с.")
        print(f"Количество сравнений: {compares}.")  # Вывод количества сравнений для данного метода.
        return min_dist  # Возврат матрицы кратчайших путей.

    # Вызов алгоритма перебора вершин.
    def shortest_path_brute_force(self, node1, node2):  # Для заданного узла node1 и другого заданного узла node2:
        return self.brute_force()[node1][node2]  # Возврат величины кратчайшего пути между node1 и node2.

    # Алгоритм Дейкстры.
    def dijkstra(self, node):
        from time import perf_counter  # Импорт perf_counter из библиотеки time.
        time_a = perf_counter()  # Время перед работой алгоритма.
        nodes_to_visit = list()  # Инициализация списка вершин для посещения.
        nodes_to_visit.append((0, node))  # Добавление стартовой вершины в список как первой вершины для посещения.
        visited = set()  # Множество для хранения посещённых вершин.
        compares = 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        min_dist = {i: float('inf') for i in range(len(self.adj_list))}  # Заполнение расстояний до вершин.
        compares += len(self.adj_list)  # Увеличение количества сравнений на количество итераций предыдущего цикла for.
        min_dist[node] = 0  # Заполнение расстояния до стартовой вершины.
        compares += 1  # Увеличение количества сравнений на 1: перед входом в цикл while.
        while len(nodes_to_visit):  # Пока nodes_to_visit не пустой:
            weight, current_node = min(nodes_to_visit)  # Выбор ближней вершины.
            nodes_to_visit.remove((weight, current_node))  # Удаление этой вершины из списка вершин для посещения.
            compares += 1  # Увеличение количества сравнений на 1: перед условием if.
            if current_node in visited:  # Если выбранная вершина уже посещена:
                # Увеличение количества сравнений на кол-во пройденных элементов списка visited.
                compares += list(visited).index(current_node)
                continue  # Запуск следующего прохода цикла без выполнения оставшегося тела цикла.
            visited.add(current_node)  # Добавление выбранной вершины в список посещённых.
            # next_weight - вес из текущей вершины, next_node - прикреплённая вершина, в которую необходимо попасть.
            compares += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for next_node, next_weight in self.adj_list[current_node]:  # Проход по всем соединённым вершинам.
                # Проверка на оптимальность пути.
                compares += 1  # Увеличение количества сравнений на 1: перед условием if.
                if weight + next_weight < min_dist[next_node] and next_node not in visited:
                    min_dist[next_node] = weight + next_weight  # Обновление расстояния.
                    nodes_to_visit.append((weight + next_weight, next_node))  # Добавление в список для посещения.
                compares += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            compares += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла while.
        time_b = perf_counter()  # Время после работы алгоритма.
        print(f"Затраченное время на работу алгоритма: {time_b - time_a:0.7f} с.")
        print(f"Количество сравнений: {compares}.")
        return min_dist  # Возврат множества из словарей {номер_узла: кратчайший путь до него от заданного узла}.

    # Вызов алгоритма Дейкстры.
    def shortest_path_dijkstra(self, node1, node2):  # Для заданного узла node1 и другого заданного узла node2:
        return self.dijkstra(node1)[node2]  # Возврат величины кратчайшего пути между node1 и node2.

    # Приложение для нахождения величины кратчайшего пути для черепашки в поле, размером m * n.
    def app_shortest_path(self, hor_edges, vert_edges):  # Для заданных списков горизонтальных и вертикальных рёбер:
        for node in range(self.vertexes):  # Для каждой вершины:
            if node < self.vertexes - self.hor_vertex:  # Если вершина не на нижней границе поля:
                if (node + 1) % self.hor_vertex != 0 or node == 0:  # Если вершина не на правой границе поля:
                    # Соединение текущей вершины с соседней справа.
                    self.connect(node, node + 1, hor_edges[node - (node + 1) // self.hor_vertex])
                    # Соединение соседней снизу вершины с текущей.
                    self.connect(node + self.hor_vertex, node, vert_edges[node])
                else:  # Иначе (если вершина на правой границе поля):
                    # Соединение только соседней снизу вершины с текущей.
                    self.connect(node + self.hor_vertex, node, vert_edges[node])
            elif node < self.vertexes - 1:  # Иначе, если вершина не последняя (но на нижней границе поля):
                # Соединение текущей вершины только с соседней справа.
                self.connect(node, node + 1, hor_edges[node - (node + 1) // self.hor_vertex])
        start_node = self.vertexes - 1 - n  # Стартовая вершина для черепашки.
        end_node = n  # Конечная вершина для черепашки.
        '''# Вывод графа в виде списка смежных вершин.
        for row in self.adj_list:  # Для каждой строки в списке смежных вершин:
            print(row)  # Вывод текущей строки списка смежных вершин.
        # Вывод графа в виде матрицы смежности.
        for row in self.adj_mat:  # Для каждой строки в матрцие смежности:
            print(row)  # Вывод текущей строки списка матрицы смежности.'''
        print('Рассмотрим метод "грубой силы" для поиска кратчайшего пути.')
        print(f'Величина кратчайшего пути: {self.shortest_path_brute_force(start_node, end_node)}.')
        print('Рассмотрим один из методов динамического программирования для поиска кратчайшего пути.')
        print(f'Величина кратчайшего пути: {self.shortest_path_dijkstra(start_node, end_node)}.')


# Главная функция.
if __name__ == '__main__':
    size = list(map(int, input("Введите размер поля m * n в формате 'm n': ").split()))  # Задание размера поля.
    m = size[0]  # Количество строк (количество рёбер в строке = количество вершин в строке - 1).
    n = size[1]  # Количество столбцов (количество столбцов в строке = количество вершин в стоблце - 1).
    w_graph = Graph(m, n)  # Создание пустого графа заданного размера.
    input_type = bool(int(input("Введите '1', если хотите ввести данные вручную, или '0', "
                                "чтобы создать случайное поле заданного размера: ")))
    if input_type is True:  # При вводе '1' данные будут введены вручную:
        print("Построчно вводите веса рёбер слева направо.")
        hor_edges = list()  # Список горизонтальных рёбер.
        vert_edges = list()  # Список вертикальных рёбер.
        for i in range(m):  # Для каждой строки поля:
            row_hor_edges = list(map(int, input(f"Введите верхние горизонтальные рёбра {i + 1}-й строки: ").split()))
            row_vert_edges = list(map(int, input(f"Введите вертикальные рёбра {i + 1}-й строки: ").split()))
            # Добавление полученных верхних горизонтальных рёбер в общий список горизонтальных рёбер.
            for element in range(n):
                hor_edges.append(row_hor_edges[element])
            # Добавление полученных вертикальных рёбер в общий список вертикальных рёбер.
            for element in range(n + 1):
                vert_edges.append(row_vert_edges[element])
        row_hor_edges = list(map(int, input(f"Введите нижние горизонтальные рёбра {m}-й строки: ").split()))
        # Добавление полученных нижних горизонтальных рёбер в общий список горизонтальных рёбер.
        for element in range(n):
            hor_edges.append(row_hor_edges[element])
    else:  # При вводе '0' данные будут сгенерированы случайным образом:
        import random  # Импорт библиотеки random.
        hor_edges = list()  # Список горизонтальных рёбер.
        vert_edges = list()  # Список вертикальных рёбер.
        for i in range(m):  # Для каждой строки поля:
            # Добавление верхних горизонтальных рёбер в общий список горизонтальных рёбер.
            for element in range(n):
                hor_edges.append(random.randint(1, 10))  # Добавление ребра со случайным весом от 1 до 10 включительно.
            # Добавление вертикальных рёбер в общий список вертикальных рёбер.
            for element in range(n + 1):
                vert_edges.append(random.randint(1, 10))  # Добавление ребра со случайным весом от 1 до 10 включительно.
        # Добавление нижних горизонтальных рёбер в общий список горизонтальных рёбер.
        for element in range(n):
            hor_edges.append(random.randint(1, 10))  # Добавление ребра со случайным весом от 1 до 10 включительно.
    print("Данные получены. Определяется кратчайший путь для черепашки из точки А в точку B.")
    w_graph.app_shortest_path(hor_edges, vert_edges)  # Нахождение величины кратчайшего пути для черепашки.
    print()
    print("Тестирование завершено.")
