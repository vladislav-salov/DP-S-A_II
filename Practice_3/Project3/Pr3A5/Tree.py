class Tree:
    def __init__(self, elements: str):
        elements = [float(x) for x in elements.split()]
        elements.sort()
        self.__start = Node(elements)

    def __str__(self):
        if self.__start == None: return ''
        ls = []
        self.__start.add_to_hor_list(ls, 0)
        return '\n'.join(ls)

    def calculate_average(self, elements: str) -> int:
        elements = [float(x) for x in elements.split()]
        elements.sort()
        middle = len(elements) // 2
        sum_left = sum_right = 0.0
        count_left = count_right = 0.0
        for i in elements[0: middle]:
            sum_left += i
            count_left += 1
        for i in elements[middle + 1:]:
            sum_right += i
            count_right += 1
        average_left = sum_left / count_left
        average_right = sum_right / count_right
        return [average_left, average_right]

    def delete(self) -> None:
        self.__start = None

class Node:
    def __init__(self, members: list):
        if len(members) == 0:
            pass
        elif len(members) == 1:
            self.info = members[0]
            self.right = None
            self.left = None
        elif len(members) == 2:
            self.info = members[1]
            self.left = Node([members[0]])
            self.right = None
        else:
            middle = len(members) // 2
            self.left = Node(members[0: middle])
            self.info = members[middle]
            self.right = Node(members[middle + 1:])

    def add_to_hor_list(self, ls: list, depth: int) -> None:
        if self.right is not None:
            self.right.add_to_hor_list(ls, depth + 1)
        ls.append('        ' * depth + str(self.info))
        if self.left is not None:
            self.left.add_to_hor_list(ls, depth + 1)