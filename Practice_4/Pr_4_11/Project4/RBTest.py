from RBTree import RBTree as Tree
import RBTree
from FileHandler import FileHandler
from Combining import Combining


def test():
    # Генератор случайных чисел для заполнения файла.
    import random  # Импорт библиотеки random.
    numbers = list(range(1103030000, 1103040000))  # Список с номерами поездов (от 1103030000 до 1103040000).
    random.shuffle(numbers)  # Перемешивание списка.
    f = open('data.txt', 'w')  # Открытие файла "data.txt" на запись.
    i = 0  # Для первой записи в номер_поезда будет записан первый элемент из списка numbers.
    for x in range(10000):  # Повторять 10000 раз:
        # Запись в строку "номер_поезда;место_отправления;место_прибытия;время_отправления".
        f.write(str(numbers[i]) + ';' + 'Place' + str(random.randint(1, 5000)) + ';' +
                'Place' + str(random.randint(5001, 9999)) + ';' + 'Time' + str(random.randint(1, 9999)) + "\n")
        i += 1  # Для следующей записи в номер_поезда будет записан следующий элемент из списка numbers.
    f.close()  # Закрытие файла "data.txt".

    # Создание объекта для работы с файлом с четырьмя полями.
    fw = FileHandler('data.bin', {'key': 11, 'place1': 10, 'place2': 10, 'time1': 9})
    tree = Tree()  # Создание дерева.
    comb = Combining(tree, fw)  # Объединение работы файла и дерева.
    fill_comb(comb, 'data.txt')  # Заполнение из файла.
    print(comb.combining)  # Вывод дерева.
    # Получение данных по ключу.
    print("Получение первой записи:")
    print(comb.get(str(numbers[0])))  # Первая запись из файла.
    print(f'Число произведённых сравнений при получении первой записи: {RBTree.compares}')
    print()  # Вывод пустой строки для визуального разделения выходных данных.
    print("Получение последней записи:")
    print(comb.get(str(numbers[9999])))  # Последняя запись из файла.
    print(f'Число произведённых сравнений при получении последней записи: {RBTree.compares}')
    print()
    print("Получение записи, расположенной в середине файла:")
    print(comb.get(str(numbers[4999])))  # Запись, расположенная в середине файла.
    print(f'Число произведённых сравнений при получении записи, расположенной в середине файла: {RBTree.compares}')
    print()
    # Получение количества произведённых поворотов.
    print(f'Общее число произведённых поворотов: {RBTree.turns}')


def fill_comb(comb: 'Combining', path: str):
    with open(path, 'r') as f:
        for line in f:
            line = line.split(';')
            comb.add(key=line[0], place1=line[1], place2=line[2], time1=line[3])


if __name__ == '__main__':
    test()
