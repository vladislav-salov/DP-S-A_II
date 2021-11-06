class Node:
    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        # Матрица смежности.
        self.adj_matrix = [[None] * col for _ in range(row)]
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if i == j:
                    self.adj_matrix[i][j] = 0
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    # Операция вставки ребра в граф.
    def connect(self, node1, node2, weight):
        node1, node2 = self.get_index(node1), self.get_index(node2)
        self.adj_matrix[node1][node2] = weight

    # Получение индекса узла.
    @staticmethod
    def get_index(node):
        if isinstance(node, int):
            return node
        else:
            return node.index

    # Алгоритм Дейкстры.
    def dijkstra(self, node):
        node = self.get_index(node)
        from collections import defaultdict
        graph = defaultdict(list)  # Инициализация графа словарём.
        # Заполнение графа по матрице смежности.
        for row in range(len(self.adj_matrix)):
            for col in range(len(self.adj_matrix)):
                if self.adj_matrix[row][col] is not None and self.adj_matrix[row][col] != 0:
                    graph[row] += [(self.adj_matrix[row][col], col)]
        nodes_to_visit = []  # Инициализация списка вершин для посещения.
        nodes_to_visit.append((0, node))  # Добавление стартовой вершины в список как первой вершины для посещения.
        visited = set()  # Множество для хранения посещённых вершин.
        min_dist = {i: float('inf') for i in range(len(self.adj_matrix))}  # Заполнение расстояний до вершин.
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
        visited = [None] * len(self.adj_matrix)  # Массив посещённых вершин.
        node1 = self.get_index(node1)
        node2 = self.get_index(node2)
        visited[0] = node2 + 1  # Начальный элемент - конечная вершина.
        pre = 1  # Индекс предыдущей вершины.
        weight = self.shortest_path(node1, node2)  # Вес конечной вершины.
        while node2 != node1:  # Пока не дошли до начальной вершины:
            for i in range(len(self.adj_matrix)):  # Проход по всем вершинам.
                if self.adj_matrix[i][node2] is not None and self.adj_matrix[i][node2] != 0:  # При наличии связи:
                    temp = weight - self.adj_matrix[i][node2]  # Определение веса пути из предыдущей вершины.
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
        node2 = self.get_index(node2)
        return self.dijkstra(node1)[node2]

    # Нахождение медианы.
    def median(self):
        array = []  # Массив из сумм кратчайших путей для каждой вершины.
        for node1 in range(len(self.adj_matrix)):
            paths_sum = 0
            for node2 in range(len(self.adj_matrix)):
                paths_sum += self.shortest_path(node1, node2)
            array.append(paths_sum)
        return array.index(min(array))

    # Приложение для ввода графа через консоль и вывода его матрицы смежности.
    def app_adj_matrix(self, directed=True):
        print("Операции вставки в граф взвешенного ребра:")
        while True:
            connection = list(map(int, input().split()))
            if not connection:
                break
            if directed is True:
                self.connect(connection[0] - 1, connection[1] - 1, connection[2])
            else:
                self.connect(connection[0] - 1, connection[1] - 1, connection[2])
                self.connect(connection[1] - 1, connection[0] - 1, connection[2])
        print("Матрица смежности графа:")
        for row in self.adj_matrix:
            print(row)

    # Приложение для нахождения кратчайшего пути от заданной вершины к другой заданной вершине и его величины.
    @staticmethod
    def app_shortest_path():
        print("Алгоритм Дейкстры поиска кратчайшего пути.")
        start_node = int(input("Номер начальной вершины: ")) - 1
        end_node = int(input("Номер конечной вершины: ")) - 1
        print("Величина кратчайшего пути:", w_graph.shortest_path(start_node, end_node))
        if w_graph.shortest_path(start_node, end_node) != float('inf'):
            print("Кратчайший путь:", w_graph.path_restoring(start_node, end_node))
        else:
            print("Путь не существует.")

    # Приложение для нахождения медианы графа.
    @staticmethod
    def app_median():
        print("Осуществляется поиск медианы графа.")
        print("Медиана найдена: это вершина под номером", w_graph.median() + 1, '.')


# Главная функция.
if __name__ == '__main__':

    # Создание графа.
    node_list = []  # Список узлов.
    quantity = int(input("Количество вершин графа: "))
    for node in range(quantity):
        node_list.append(Node(str(node)))
    w_graph = Graph.create_from_nodes(node_list)

    # Вставка рёбер и вывод матрицы смежности.
    directed = bool(int(input("Для ориентированного графа введите '1', для неориентированного – '0': ")))
    w_graph.app_adj_matrix(directed)

    print()
    # Нахождение кратчайшего пути и его величины методом "Дейкстры".
    w_graph.app_shortest_path()

    # Нахождение медианы неориентированного графа.
    if directed is False:
        print()
        w_graph.app_median()

    print()
    print("Работа программы завершена.")
