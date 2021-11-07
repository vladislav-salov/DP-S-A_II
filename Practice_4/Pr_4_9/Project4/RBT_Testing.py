from RB_Tree import RBT
import RB_Tree
from F_Handler import FileHandler
from FS_Combining import Combining


def test():
    # Заполнение файла 10000 записями.
    import random
    numbers = list(range(2401030000, 2401040000))  # Список с номерами страховых полисов.
    random.shuffle(numbers)  # Перемешивание списка.
    f = open('Data_Records.txt', 'w')  # Открытие файла "Data_Records.txt" на запись.
    i = 0  # Для первой записи в номер_полиса будет записан первый элемент из списка numbers.
    for x in range(10000):  # Повторять 10000 раз:
        # Запись в строку: "номер_полиса;компания;фамилия_владельца".
        f.write(str(numbers[i]) + ';' + 'Company' + str(random.randint(1, 9999)) + ';'
                + 'Soname' + str(random.randint(1, 9999)) + "\n")
        i += 1  # Для следующей записи в номер_полиса будет записан следующий элемент из списка numbers.
    f.close()  # Закрытие файла "Data_Records.txt".
    # Создание объекта для работы с файлом с тремя полями.
    fw = FileHandler('Data_Records.bin', {'key': 11, 'company': 12, 'soname': 11})
    tree = RBT()  # Создание дерева.
    comb = Combining(tree, fw)  # Объединение работы файла и дерева.
    fill_comb(comb, 'Data_Records.txt')  # Заполнение из файла.
    print(comb.combining)  # Вывод дерева.
    print()
    # Количество выполненных поворотов.
    print(f'Количество выполненных поворотов: {RB_Tree.turns}')
    print()
    # Получение данных по ключу.
    print(f'Первая запись из файла: {comb.get(str(numbers[0]))}')
    print(f'Количество сравнений при получении первой записи: {RB_Tree.compares}')
    print()
    print(f'Последняя запись из файла: {comb.get(str(numbers[9999]))}')
    print(f'Количество сравнений при получении последней записи: {RB_Tree.compares}')
    print()
    print(f'Запись в середине файла: {comb.get(str(numbers[4999]))}')
    print(f'Количество сравнений при получении записи в середине файла: {RB_Tree.compares}')


def fill_comb(comb: 'Combining', path: str):
    with open(path, 'r') as f:
        for line in f:
            line = line.split(';')
            comb.add(key=line[0], company=line[1], soname=line[2])


if __name__ == '__main__':
    test()
