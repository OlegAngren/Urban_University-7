import string

class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация объекта класса.
        :param file_names: Названия файлов, переданных при создании объекта.
        """
        self.file_names = list(file_names)  # Сохраняем имена файлов в атрибут

    def get_all_words(self):
        """
        Считывает все слова из файлов и формирует словарь с названиями файлов и их словами.
        :return: Словарь {имя файла: список слов}.
        """
        all_words = {}  # Словарь для хранения результатов

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем содержимое файла и приводим к нижнему регистру
                    text = file.read().lower()

                    # Удаляем пунктуацию, заменяя её на пробелы
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(char, ' ')

                    # Разбиваем текст на слова
                    words = text.split()

                    # Записываем слова файла в словарь
                    all_words[file_name] = words

            except FileNotFoundError:
                # Если файл не найден, записываем пустой список
                all_words[file_name] = []

        return all_words

    def find(self, word):
        """
        Ищет первое вхождение слова в каждом файле.
        :param word: Искомое слово.
        :return: Словарь {имя файла: позиция слова}.
        """
        result = {}  # Словарь для хранения позиций слова
        word = word.lower()  # Приводим слово к нижнему регистру для поиска

        for file_name, words in self.get_all_words().items():
            try:
                # Находим позицию слова и сохраняем её (+1 для номерации с 1)
                position = words.index(word) + 1
                result[file_name] = position
            except ValueError:
                # Если слово не найдено, записываем None
                result[file_name] = None

        return result

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле.
        :param word: Искомое слово.
        :return: Словарь {имя файла: количество вхождений}.
        """
        result = {}  # Словарь для хранения количества вхождений
        word = word.lower()  # Приводим слово к нижнему регистру для подсчёта

        for file_name, words in self.get_all_words().items():
            # Подсчитываем количество вхождений слова в списке
            count = words.count(word)
            result[file_name] = count

        return result

# Пример использования:
# Содержимое файла 'test_file.txt':
# It's a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text

finder2 = WordsFinder('test_file.txt')

# Получение всех слов из файла
print(finder2.get_all_words())  # {'test_file.txt': [...список слов...]}

# Поиск первого вхождения слова
print(finder2.find('TEXT'))  # {'test_file.txt': 3}

# Подсчёт количества вхождений слова
print(finder2.count('teXT'))  # {'test_file.txt': 4}
