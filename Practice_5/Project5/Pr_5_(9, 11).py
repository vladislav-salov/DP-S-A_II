class Node:  # Класс узла графа.
    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class Graph:  # Класс, реализующий граф и некоторые операции с ним.

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        # Установка матрицы смежности.
        self.adj_mat = [[None] * col for _ in range(row)]
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat)):
                if i == j:
                    self.adj_mat[i][j] = 0
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    # Вставка взвешенного ребра в граф.
    def connect(self, node1, node2, weight):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight

    '''
    # Связи от элемента.
    def connections_from(self, node):
        node = self.get_index_from_node(node)
        # Возврат значения: массив кортежей (узел, вес).
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node]))
                if self.adj_mat[node][col_num] != 0 and self.adj_mat[node][col_num] is not None]

    # Связи с элементом.
    def connections_to(self, node):
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_mat]
        # Возврат значения: массив кортежей (узел, вес).
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column))
                if column[row_num] != 0 and column[row_num] is not None]

    # Узел.
    def node(self, index):
        return self.nodes[index]

    # Удаление связи от node1 к node2.
    def remove_connection(self, node1, node2):
        # Принятие номера индекса или объекта узла.
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = 0

    # Наличие связи от node1 к node2.
    def can_traverse(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2] != 0

    # Наличие какой-либо связи между элементами node1 и node2.
    def has_connection(self, node1, node2):
        return self.can_traverse(node1, node2) or self.can_traverse(node2, node1)

    # Вставка элемента в граф.
    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adj_mat:
            row.append(0)
        self.adj_mat.append([0] * (len(self.adj_mat) + 1))

    # Вес ребра (длина пути) от node1 к node2.
    def get_weight(self, node1, node2):
        # Принятие номера индекса или объекта узла.
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2]
    '''

    # Индекс узла.
    @staticmethod
    def get_index_from_node(node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("Node must be an integer or a Node object.")
        if isinstance(node, int):
            return node
        else:
            return node.index

    # Нахождение количества достижимых вершин для узла через обход "в глубину" для проверки графа на сильную связность.
    def connectivity_DFS(self, node_index, visited):
        visited.add(node_index)
        for i in range(len(self.adj_mat)):
            if self.adj_mat[node_index][i] is not None and i not in visited:
                self.connectivity_DFS(i, visited)
        return len(visited)

    # Нахождение количества достижимых вершин для узла через обход "в глубину" для проверки графа на слабую связность.
    def weak_connectivity_DFS(self, node_index, visited):
        visited.add(node_index)
        for i in range(len(self.adj_mat)):
            if ((self.adj_mat[node_index][i] is not None or self.adj_mat[i][node_index] is not None)
                    and i not in visited):
                self.weak_connectivity_DFS(i, visited)
        return len(visited)

    # Проверка на связность.
    def connectivity(self, directed):
        if not directed:
            for node_index in range(len(self.adj_mat)):
                visited = set()
                if self.connectivity_DFS(node_index, visited) < len(self.adj_mat):
                    return [False]
        else:
            for node_index in range(len(self.adj_mat)):
                visited = set()
                if self.connectivity_DFS(node_index, visited) < len(self.adj_mat):
                    if self.weak_connectivity_DFS(node_index, visited) < len(self.adj_mat):
                        return [False]
                    else:
                        return [True, False]
        return [True, True]

    # Алгоритм Дейкстры.
    def dijkstra(self, node):
        node = self.get_index_from_node(node)
        from collections import defaultdict
        graph = defaultdict(list)  # Инициализация графа словарём.
        # Заполнение графа по матрице смежности.
        for row in range(len(self.adj_mat)):
            for col in range(len(self.adj_mat)):
                if self.adj_mat[row][col] is not None and self.adj_mat[row][col] != 0:
                    graph[row] += [(self.adj_mat[row][col], col)]
        nodes_to_visit = []  # Инициализация списка вершин для посещения.
        nodes_to_visit.append((0, node))  # Добавление стартовой вершины в список как первой вершины для посещения.
        visited = set()  # Множество для хранения посещённых вершин.
        min_dist = {i: float('inf') for i in range(len(self.adj_mat))}  # Заполнение расстояний до вершин.
        min_dist[node] = 0  # Заполнение расстояния до стартовой вершины.
        while len(nodes_to_visit):  # Пока nodes_to_visit не пустой:
            weight, current_node = min(nodes_to_visit)  # Выбор ближней вершины.
            nodes_to_visit.remove((weight, current_node))  # Удаление этой вершины из списка вершин для посещения.
            if current_node in visited:  # Если выбранная вершина уже посещена:
                continue  # Запустить следующий проход цикла, не выполняя оставшееся тело цикла.
            visited.add(current_node)  # Добавление выбранной вершины в список посещённых.
            # next_weight - вес связи из текущей вершины, next_node - прикреплённая вершина, в которую необходимо попасть.
            for next_weight, next_node in graph[current_node]:  # Проход по всем соединённым вершинам.
                # Проверка на оптимальность пути.
                if weight + next_weight < min_dist[next_node] and next_node not in visited:
                    min_dist[next_node] = weight + next_weight  # Обновление расстояния.
                    nodes_to_visit.append((weight + next_weight, next_node))  # Добавление вершины в список вершин для посещения.
        return min_dist  # Возврат множества из словарей {номер_узла: кратчайший путь до него от заданного узла}.

    # Восстановление кратчайшего пути между node1 и node2.
    def path_restoring(self, node1, node2):
        visited = [None] * len(self.adj_mat)  # Массив посещённых вершин.
        node1 = self.get_index_from_node(node1)
        node2 = self.get_index_from_node(node2)
        visited[0] = node2 + 1  # Начальный элемент - конечная вершина.
        pre = 1  # Индекс предыдущей вершины.
        weight = self.shortest_path(node1, node2)  # Вес конечной вершины.
        while node2 != node1:  # Пока не дошли до начальной вершины:
            for i in range(len(self.adj_mat)):  # Проход по всем вершинам.
                if self.adj_mat[i][node2] is not None and self.adj_mat[i][node2] != 0:  # При наличии связи:
                    temp = weight - self.adj_mat[i][node2]  # Определение веса пути из предыдущей вершины.
                    if temp == self.shortest_path(node1, i):  # Если вес совпал с рассчитанным, то из этой вершины был переход.
                        weight = temp
                        node2 = i
                        visited[pre] = i + 1
                        pre += 1
        while None in visited:
            visited.remove(None)
        return visited[::-1]

    # Нахождение величины кратчайшего пути между двумя заданными вершинами.
    def shortest_path(self, node1, node2):
        node2 = self.get_index_from_node(node2)
        return self.dijkstra(node1)[node2]

    # Нахождение медианы.
    def median(self):
        array = []  # Массив из сумм кратчайших путей для каждой вершины.
        for node1 in range(len(self.adj_mat)):
            paths_sum = 0
            for node2 in range(len(self.adj_mat)):
                paths_sum += self.shortest_path(node1, node2)
            array.append(paths_sum)
        return array.index(min(array))

    # Приложение для ввода графа и вывода матрицы смежности.
    def app_adj_mat(self, directed=True):
        print("Построчно производите вставку рёбер в граф в формате:")
        print("номер начальной вершины, номер конечной вершины, вес связи")
        print("Для завершения добавления рёбер подайте на вход пустую строку.")
        print()
        while True:
            print("Ожидается ребро:")
            connection = list(map(int, input().split()))
            if not connection:
                break
            if directed is True:
                self.connect(connection[0] - 1, connection[1] - 1, connection[2])
                print("Добавлено направленное ребро от вершины", connection[0], "к вершине", connection[1], "с весом", connection[2], ".")
            else:
                self.connect(connection[0] - 1, connection[1] - 1, connection[2])
                self.connect(connection[1] - 1, connection[0] - 1, connection[2])
                print("Ребро с весом", connection[2], "успешно добавлено: вершины", connection[0], "и", connection[1], "соединены.")
        print("Вставка рёбер завершена.")
        print()
        print("Построена матрица смежности графа:")
        for row in self.adj_mat:
            print(row)

    # Приложение для нахождения кратчайшего пути от заданной вершины к другой заданной вершине и его величины.
    @staticmethod
    def app_shortest_path():  # Общее задание для вариантов 9 и 11.
        print("Рассмотрим алгоритм Дейкстры поиска кратчайшего пути.")
        start_node = int(input("Введите номер начальной вершины: ")) - 1
        end_node = int(input("Введите номер конечной вершины: ")) - 1
        print("Величина кратчайшего пути:", w_graph.shortest_path(start_node, end_node))
        if w_graph.shortest_path(start_node, end_node) != float('inf'):
            print("Кратчайший путь:", w_graph.path_restoring(start_node, end_node))
        else:
            print("Невозможно выполнить проход от заданной начальной вершины к заданной конечной вершине.")

    # Приложение для проверки графа на связность.
    @staticmethod
    def app_connectivity(directed):  # Задание варианта 11.
        print("Выполняется проверка графа на связность.")
        if w_graph.connectivity(directed)[0] is False:
            print("Результат проверки: граф не является связным.")
        elif w_graph.connectivity(directed)[1] is True:
            if directed is True:
                print("Результат проверки: граф является сильно связным.")
            else:
                print("Результат проверки: граф является связным.")
        else:
            print("Результат проверки: граф является слабо связным.")

    # Приложение для нахождения медианы графа.
    @staticmethod
    def app_median():  # Задание варианта 9.
        print("Осуществляется поиск медианы графа.")
        print("Медиана найдена: это вершина под номером", w_graph.median() + 1, '.')


# Главная функция.
if __name__ == '__main__':

    # Создание графа.
    node_list = []  # Список узлов.
    quantity = int(input("Введите количество вершин графа: "))
    for node in range(quantity):
        node_list.append(Node(str(node)))
    w_graph = Graph.create_from_nodes(node_list)

    # Вставка рёбер и вывод матрицы смежности.
    directed = bool(int(input("Если граф – ориентированный, то введите '1', иначе – введите '0': ")))
    w_graph.app_adj_mat(directed)

    print()
    # Нахождение кратчайшего пути и его величины методом "Дейкстры".
    w_graph.app_shortest_path()

    print()
    # Проверка графа на связность.
    w_graph.app_connectivity(directed)

    # Нахождение медианы неориентированного графа.
    if directed is False:
        print()
        w_graph.app_median()

    print()
    print("Тестирование завершено.")
