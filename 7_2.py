def custom_write(file_name, strings):
    """
    Записывает строки в файл и возвращает словарь с позициями строк.

    :param file_name: Имя файла для записи.
    :param strings: Список строк для записи в файл.
    :return: Словарь с информацией о строках и их позициях в файле.
    """
    strings_positions = {}  # Словарь для хранения позиций строк

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию байта перед записью строки
            byte_position = file.tell()

            # Записываем строку с символом новой строки
            file.write(string + '\n')

            # Сохраняем информацию о строке и её позиции в словарь
            strings_positions[(line_number, byte_position)] = string

    return strings_positions


# Пример использования функции:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим результат на консоль
for elem in result.items():
    print(elem)
