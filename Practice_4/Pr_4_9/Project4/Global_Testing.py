from BS_Tree import BST
import BS_Tree
from RB_Tree import RBT
import RB_Tree
from Hash_Table import HT
import Hash_Table
from F_Handler import FileHandler
from FS_Combining import Combining


def test():
    print("--- Заполнение файла 1000 записями. ---")
    print()
    import random
    numbers = list(range(240103000, 240104000))  # Список с номерами страховых полисов.
    random.shuffle(numbers)  # Перемешивание списка.
    f = open('Data_Records.txt', 'w')  # Открытие файла "Data_Records.txt" на запись.
    i = 0  # Для первой записи в номер_полиса будет записан первый элемент из списка numbers.
    for x in range(1000):  # Повторять 1000 раз:
        # Запись в строку: "номер_полиса;компания;фамилия_владельца".
        f.write(str(numbers[i]) + ';' + 'Company' + str(random.randint(1, 999)) + ';'
                + 'Soname' + str(random.randint(1, 999)) + "\n")
        i += 1  # Для следующей записи в номер_полиса будет записан следующий элемент из списка numbers.
    f.close()  # Закрытие файла "Data_Records.txt".
    # Создание объекта для работы с файлом с тремя полями.
    fw = FileHandler('Data_Records.bin', {'key': 11, 'company': 12, 'soname': 11})
    bs = BST()  # Создание БДП.
    rb = RBT()  # Создание СДП.
    ht = HT()  # Создание хеш-таблицы.
    bs_comb = Combining(bs, fw)  # Объединение работы файла и БДП.
    rb_comb = Combining(rb, fw)  # Объединение работы файла и СДП.
    ht_comb = Combining(ht, fw)  # Объединение работы файла и хеш-таблицы.
    fill_comb(bs_comb, 'Data_Records.txt')  # Заполнение БДП из файла.
    fill_comb(rb_comb, 'Data_Records.txt')  # Заполнение СДП из файла.
    fill_comb(ht_comb, 'Data_Records.txt')  # Заполнение хеш-таблицы из файла.
    # print(bs_comb.combining)  # Вывод БДП.
    # print(rb_comb.combining)  # Вывод СДП.
    # HT.print()  # Вывод хеш-таблицы.

    # Получение первой записи файла по ключу.
    print(">>> Первая запись <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()

    # Получение последней записи файла по ключу.
    print(">>> Последняя запись <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[999]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[999]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[999]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()

    # Получение по ключу записи, расположенной в середине файла.
    print(">>> Запись в середине файла <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[499]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[499]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[499]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()

    # from time import sleep
    # sleep(10)  # Перерыв, чтобы успеть заскринить предыдущие записи в файле.

    print("--- Заполнение файла 10000 записями. ---")
    print()
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
    bs = BST()  # Создание БДП.
    rb = RBT()  # Создание СДП.
    ht = HT()  # Создание хеш-таблицы.
    bs_comb = Combining(bs, fw)  # Объединение работы файла и БДП.
    rb_comb = Combining(rb, fw)  # Объединение работы файла и СДП.
    ht_comb = Combining(ht, fw)  # Объединение работы файла и хеш-таблицы.
    fill_comb(bs_comb, 'Data_Records.txt')  # Заполнение БДП из файла.
    fill_comb(rb_comb, 'Data_Records.txt')  # Заполнение СДП из файла.
    fill_comb(ht_comb, 'Data_Records.txt')  # Заполнение хеш-таблицы из файла.
    # print(bs_comb.combining)  # Вывод БДП.
    # print(rb_comb.combining)  # Вывод СДП.
    # HT.print()  # Вывод хеш-таблицы.

    # Получение первой записи файла по ключу.
    print(">>> Первая запись <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[0]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()

    # Получение последней записи файла по ключу.
    print(">>> Последняя запись <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[9999]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[9999]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[9999]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()

    # Получение по ключу записи, расположенной в середине файла.
    print(">>> Запись в середине файла <<<")
    print()
    print("С помощью БДП:")
    bs_comb.get(str(numbers[4999]))
    print(f'Количество сравнений: {BS_Tree.compares}')
    print()
    print("С помощью СДП:")
    rb_comb.get(str(numbers[4999]))
    print(f'Количество сравнений: {RB_Tree.compares}')
    print()
    print("С помощью хеш-таблицы:")
    ht_comb.get(str(numbers[4999]))
    print(f'Количество сравнений: {Hash_Table.compares}')
    print()


def fill_comb(comb: 'Combining', path: str):
    with open(path, 'r') as f:
        for line in f:
            line = line.split(';')
            comb.add(key=line[0], company=line[1], soname=line[2])


if __name__ == '__main__':
    test()
