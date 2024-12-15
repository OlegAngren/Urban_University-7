import os
import time

# Путь к каталогу, который мы хотим обойти.
# Для тестов установим путь к текущему каталогу.
directory = "."

# os.walk обходит каталог рекурсивно, начиная с directory.
# На каждой итерации root - текущая директория,
# dirs - список вложенных папок, files - список файлов в текущей директории.
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу с помощью os.path.join
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Преобразуем время в читаемый формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
