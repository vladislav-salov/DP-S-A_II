from collections import deque

class Tree:
    def __init__(self, elements: str):
        elements = [str(x) for x in elements.split()]
        elements.sort()
        self.__start = Node(elements)

    def __str__(self):
        if self.__start == None: return ''
        ls = []
        self.__start.add_to_hor_list(ls, 0)
        return '\n'.join(ls)

    def count_digits_from_left(self, elements: str) -> int:
        elements = [str(x) for x in elements.split()]
        elements.sort()
        middle = len(elements) // 2
        sum_d = 0
        for i in elements[0: middle]:
            for j in i:
                if (j <= '9') and (j >= '0'):
                    sum_d += 1
        return sum_d

    def delete(self) -> None:
        self.__start = None

    def print_vert(self):
        if self.__start == None: return ''
        ls = []
        depth = self.__start.add_to_vert_list(ls, 0)
        res = ''
        for line in range(depth + 1):
            for pos in range(len(ls)):
                if ls[pos][1] == line:
                    res += str(ls[pos][0])
                else:
                    res += ' ' * ls[pos][2]
            res += '\n'
        return res

    def level(self, key: str, elements: str):
        elements = [str(x) for x in elements.split()]
        if key not in elements: return('–')
        else: return self.__start.dfs(0, key)


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
        ls.append('        ' * depth + str(self.info) + '(' + str(depth) + ')')
        if self.left is not None:
            self.left.add_to_hor_list(ls, depth + 1)

    def add_to_vert_list(self, ls: list, depth) -> int:
        m1, m2 = 0, 0
        if self.left is not None:
            m1 = self.left.add_to_vert_list(ls, depth + 1)
        ls.append((self.info, depth, len(str(self.info))))
        if self.right is not None:
            m2 = self.right.add_to_vert_list(ls, depth + 1)
        return max(m1, m2, depth)

    def dfs(self, depth, key):
        res = 0
        if self.right is not None:
            res += self.right.dfs(depth + 1, key)
        if self.left is not None:
            res += self.left.dfs(depth + 1, key)
        return res if self.info != key else depth