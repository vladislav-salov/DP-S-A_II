# Класс, реализующий граф и некоторые операции с ним.
class Graph:
    # Конструктор класса.
    def __init__(self, m, n, start_weight):
        self.start_weight = start_weight  # Вес первой вершины, который не учитывается при построении графа.
        self.compares_bf = 0  # Количество сравнений при работе метода "грубой силы".
        self.compares_dp = 0  # Количество сравнений при работе метода динамического программирования.
        self.vert_vertex = m  # Количество вершин графа по вертикали.
        self.hor_vertex = n  # Количество вершин графа по горизонтали.
        self.vertexes = self.hor_vertex * self.vert_vertex  # Общее количество вершин графа.
        # Установка списка смежных вершин.
        self.adj_list = list()
        for i in range(self.vertexes):
            self.adj_list.append([])
        # Установка матрицы смежности.
        self.adj_mat = [[float('inf')] * self.vertexes for _ in range(self.vertexes)]
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat)):
                if i == j:
                    self.adj_mat[i][j] = 0

    # Процедура вставки взвешенного ребра в граф.
    def connect(self, node1, node2, weight):
        self.adj_list[node1].append([node2, weight])  # Вставка ребра в список смежных вершин.
        self.adj_mat[node1][node2] = weight  # Вставка ребра в матрицу смежности для алгоритма перебора вершин.

    # Функция копирования матрицы смежности для дальнейшего перезаполнения под матрицу кратчайших путей.
    def adj_mat_copy(self):
        adj_matrix = [[None] * self.vertexes for _ in range(self.vertexes)]
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat)):
                adj_matrix[i][j] = self.adj_mat[i][j]
        return adj_matrix

    # Функция алгоритма перебора вершин (метода "грубой силы").
    def brute_force(self):
        v = len(self.adj_mat)  # Количество узлов графа как длина матрицы смежности.
        min_dist = self.adj_mat_copy()  # Матрица кратчайших путей, изначально являющаяся копией матрицы смежности.
        self.compares_bf += 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        for k in range(v):
            self.compares_bf += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for i in range(v):
                self.compares_bf += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
                for j in range(v):
                    self.compares_bf += 1  # Увеличение количества сравнений на 1: перед условием if.
                    if min_dist[i][j] > min_dist[i][k] + min_dist[k][j]:
                        min_dist[i][j] = min_dist[i][k] + min_dist[k][j]  # Величина текущего кратчайшего пути из i в j.
                    self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
                self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
        return min_dist  # Возврат матрицы кратчайших путей.

    # Функция величины кратчайшего пути, методом перебора вершин ("грубой силы").
    def shortest_path_brute_force(self, node1, node2):  # Для заданного узла node1 и другого заданного узла node2:
        # Возврат величины кратчайшего пути между node1 и node2.
        return self.brute_force()[node1][node2] + self.start_weight

    # Функция восстановления кратчайшего пути между двумя заданными вершинами, методом перебора вершин ("грубой силы").
    def path_restoring_brute_force(self, node1, node2):
        visited = list()
        self.compares_bf += 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        for i in range(len(self.adj_mat)):
            self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            visited.append((None, None))
        # Начальный элемент - конечная вершина. Добавление в список номера элемента матрицы.
        visited[0] = (node2 // self.hor_vertex + 1, node2 % self.hor_vertex + 1)
        pre = 1  # Индекс предыдущей вершины.
        weight = self.shortest_path_brute_force(node1, node2) - self.start_weight  # Вес пути до конечной вершины.
        self.compares_bf += 1  # Увеличение количества сравнений на 1: перед входом в цикл while.
        while node2 != node1:  # Пока не дошли до начальной вершины:
            self.compares_bf += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for i in range(len(self.adj_mat)):  # Проход по всем вершинам.
                self.compares_bf += 2  # Увеличение количества сравнений на 2: перед условием if.
                if self.adj_mat[i][node2] < float('inf') and self.adj_mat[i][node2] != 0:  # При наличии связи:
                    temp = weight - self.adj_mat[i][node2]  # Определение веса пути из предыдущей вершины.
                    self.compares_bf += 1  # Увеличение количества сравнений на 1: перед условием if.
                    # Если вес совпал с рассчитанным, то из этой вершины был переход.
                    if temp == self.shortest_path_brute_force(node1, i) - self.start_weight:
                        weight = temp
                        node2 = i
                        visited[pre] = (i // self.hor_vertex + 1, i % self.hor_vertex + 1)
                        pre += 1
                self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            self.compares_bf += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла while.
        self.compares_bf += len(visited)  # Увеличение кол-ва сравнений на кол-во пройденных элементов списка visited.
        while (None, None) in visited:
            # Увеличение кол-ва сравнений на кол-во пройденных элементов списка visited.
            self.compares_bf += list(visited).index((None, None))
            visited.remove((None, None))
        return visited[::-1]

    # Алгоритм Дейкстры.
    def dijkstra(self, node):
        nodes_to_visit = list()  # Инициализация списка вершин для посещения.
        nodes_to_visit.append((0, node))  # Добавление стартовой вершины в список как первой вершины для посещения.
        visited = set()  # Множество для хранения посещённых вершин.
        self.compares_dp += 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        min_dist = {i: float('inf') for i in range(len(self.adj_list))}  # Заполнение расстояний до вершин.
        self.compares_dp += len(self.adj_list)  # Увеличение кол-ва сравнений на кол-во итераций предыдущего цикла for.
        min_dist[node] = 0  # Заполнение расстояния до стартовой вершины.
        self.compares_dp += 1  # Увеличение количества сравнений на 1: перед входом в цикл while.
        while len(nodes_to_visit):  # Пока nodes_to_visit не пустой:
            self.compares_dp += len(nodes_to_visit)  # Увеличение кол-ва сравнений на кол-во итераций для функции min().
            weight, current_node = min(nodes_to_visit)  # Выбор ближней вершины.
            nodes_to_visit.remove((weight, current_node))  # Удаление этой вершины из списка вершин для посещения.
            if current_node in visited:  # Если выбранная вершина уже посещена:
                # Увеличение количества сравнений на кол-во пройденных элементов списка visited.
                self.compares_dp += list(visited).index(current_node)
                continue  # Запуск следующего прохода цикла без выполнения оставшегося тела цикла.
            # Увеличение кол-ва сравнений на на кол-во пройденных элементов списка visited.
            self.compares_dp += len(list(visited))
            visited.add(current_node)  # Добавление выбранной вершины в список посещённых.
            # next_weight - вес из текущей вершины, next_node - прикреплённая вершина, в которую необходимо попасть.
            self.compares_dp += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for next_node, next_weight in self.adj_list[current_node]:  # Проход по всем соединённым вершинам.
                # Проверка на оптимальность пути.
                if next_node in visited:
                    # Увеличение количества сравнений на кол-во пройденных элементов списка visited в следующем "if".
                    self.compares_dp += list(visited).index(next_node)
                self.compares_dp += 1  # Увеличение количества сравнений на 1: перед условием if.
                if weight + next_weight < min_dist[next_node] and next_node not in visited:
                    # Увеличение количества сравнений на кол-во пройденных элементов списка visited.
                    self.compares_dp += len(list(visited))
                    min_dist[next_node] = weight + next_weight  # Обновление расстояния.
                    nodes_to_visit.append((weight + next_weight, next_node))  # Добавление в список для посещения.
                self.compares_dp += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            self.compares_dp += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла while.
        return min_dist  # Возврат множества из словарей {номер_узла: кратчайший путь до него от заданного узла}.

    # Функция величины кратчайшего пути, методом "Дейкстры".
    def shortest_path_dijkstra(self, node1, node2):  # Для заданного узла node1 и другого заданного узла node2:
        return self.dijkstra(node1)[node2] + self.start_weight  # Возврат величины кратчайшего пути между node1 и node2.

    # Функция восстановления кратчайшего пути между двумя заданными вершинами, методом "Дейкстры".
    def path_restoring_dijkstra(self, node1, node2):
        visited = list()
        self.compares_dp += 1  # Подсчёт количества сравнений: первое сравнение перед входом в цикл for.
        for i in range(len(self.adj_mat)):
            self.compares_dp += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            visited.append((None, None))
        # Начальный элемент - конечная вершина. Добавление в список номера элемента матрицы.
        visited[0] = (node2 // self.hor_vertex + 1, node2 % self.hor_vertex + 1)
        pre = 1  # Индекс предыдущей вершины.
        weight = self.shortest_path_dijkstra(node1, node2) - self.start_weight  # Вес пути до конечной вершины.
        self.compares_dp += 1  # Увеличение количества сравнений на 1: перед входом в цикл while.
        while node2 != node1:  # Пока не дошли до начальной вершины:
            self.compares_dp += 1  # Увеличение количества сравнений на 1: перед входом в цикл for.
            for i in range(len(self.adj_mat)):  # Проход по всем вершинам.
                self.compares_dp += 2  # Увеличение количества сравнений на 2: перед условием if.
                if self.adj_mat[i][node2] < float('inf') and self.adj_mat[i][node2] != 0:  # При наличии связи:
                    temp = weight - self.adj_mat[i][node2]  # Определение веса пути из предыдущей вершины.
                    self.compares_dp += 1  # Увеличение количества сравнений на 1: перед условием if.
                    # Если вес совпал с рассчитанным, то из этой вершины был переход.
                    if temp == self.shortest_path_dijkstra(node1, i) - self.start_weight:
                        weight = temp
                        node2 = i
                        visited[pre] = (i // self.hor_vertex + 1, i % self.hor_vertex + 1)
                        pre += 1
                self.compares_dp += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла for.
            self.compares_dp += 1  # Увеличение количества сравнений на 1: с каждой итерацией цикла while.
        self.compares_dp += len(visited)  # Увеличение кол-ва сравнений на кол-во пройденных элементов списка visited.
        while (None, None) in visited:
            # Увеличение кол-ва сравнений на кол-во пройденных элементов списка visited.
            self.compares_dp += list(visited).index((None, None))
            visited.remove((None, None))
        return visited[::-1]

    # Приложение для нахождения величины кратчайшего пути для черепашки в поле, размером m * n.
    def app_shortest_path(self, matrix_elements):  # Для заданного списка элементов матрицы:
        for node in range(self.vertexes):  # Для каждой вершины:
            if node < self.vertexes - self.hor_vertex:  # Если вершина не на нижней границе поля:
                # Соединение текущей вершины с соседней снизу.
                self.connect(node, node + self.hor_vertex, matrix_elements[node + self.hor_vertex])
                if (node + 1) % self.hor_vertex != 0 or node == 0:  # Если вершина не на правой границе поля:
                    # Соединение текущей вершины с вершиной снизу справа по диагонали.
                    self.connect(node, node + self.hor_vertex + 1, matrix_elements[node + self.hor_vertex + 1])
                    # Соединение текущей вершины с соседней справа.
                    self.connect(node, node + 1, matrix_elements[node + 1])
            elif node < self.vertexes - 1:  # Иначе, если вершина не последняя (но на нижней границе поля):
                # Соединение текущей вершины только с соседней справа.
                self.connect(node, node + 1, matrix_elements[node + 1])
        '''# Вывод графа в виде списка смежных вершин.
        for row in self.adj_list:  # Для каждой строки в списке смежных вершин:
            print(row)  # Вывод текущей строки списка смежных вершин.
        # Вывод графа в виде матрицы смежности.
        for row in self.adj_mat:  # Для каждой строки в матрцие смежности:
            print(row)  # Вывод текущей строки списка матрицы смежности.'''
        from time import perf_counter  # Импорт perf_counter из библиотеки time.
        print("________________________________________________________________________________________________")
        print('Метод "грубой силы" для поиска кратчайшего пути.')
        time_a = perf_counter()  # Время перед работой алгоритма.
        print(f'Величина кратчайшего пути: {self.shortest_path_brute_force(0, self.vertexes - 1)}.')
        print(f'Кратчайший маршрут: {self.path_restoring_brute_force(0, self.vertexes - 1)}.')
        time_b = perf_counter()  # Время после работы алгоритма.
        print(f"Затраченное время на работу алгоритма: {time_b - time_a:0.7f} с.")
        print(f'Количество выполненных сравнений: {self.compares_bf}.')
        print("________________________________________________________________________________________________")
        print('Метод "Дейкстры" как один из методов динамического программирования для поиска кратчайшего пути.')
        time_a = perf_counter()  # Время перед работой алгоритма.
        print(f'Величина кратчайшего пути: {self.shortest_path_dijkstra(0, self.vertexes - 1)}.')
        print(f'Кратчайший маршрут: {self.path_restoring_dijkstra(0, self.vertexes - 1)}.')
        time_b = perf_counter()  # Время после работы алгоритма.
        print(f"Затраченное время на работу алгоритма: {time_b - time_a:0.7f} с.")
        print(f'Количество выполненных сравнений: {self.compares_dp}.')
        print("________________________________________________________________________________________________")


# Главная функция.
if __name__ == '__main__':
    matrix_elements = list()  # Список элементов матрицы (весов клеток поля).
    size = list(map(int, input('Укажите размер матрицы m * n в виде "m n": ').split()))  # Задание размера матрицы.
    m = size[0]  # Количество строк матрицы.
    n = size[1]  # Количество столбцов матрицы.
    print("Введите число для выбора типа ввода данных:\n"
          "0 – установка веса для каждой клетки вручную;\n"
          "1 – автоматическая установка случайного веса для каждой клетки.")
    input_type = bool(int(input("Ваше число: ")))
    if input_type is True:  # При вводе '1' данные будут введены автоматически (сгенерированы случайным образом):
        import random  # Импорт библиотеки random.
        # Заполнение матрицы случайными числами от 1 до 10.
        for element in range(m * n):
            matrix_elements.append(random.randint(1, 10))
    else:  # При вводе '0' данные будут введены вручную:
        print("Построчно вводите элементы матрицы слева направо.")
        for i in range(m):  # Для каждой строки матрицы:
            matrix_row_elements = list(map(int, input(f"Введите элементы {i + 1}-й строки матрицы: ").split()))
            # Добавление введённых элементов в матрицу.
            for element in range(n):
                matrix_elements.append(matrix_row_elements[element])
    print("Данные получены. Определяется кратчайший путь от первого элемента матрицы к последнему.")
    w_graph = Graph(m, n, matrix_elements[0])  # Создание пустого графа заданного размера.
    w_graph.app_shortest_path(matrix_elements)  # Нахождение величины кратчайшего пути от первого элемента к последнему.
    print()
    print("Тестирование завершено.")
