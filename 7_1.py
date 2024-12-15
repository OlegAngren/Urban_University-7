class Product:
    def __init__(self, name, weight, category):
        # Инициализация атрибутов товара
        self.name = name  # Название продукта
        self.weight = weight  # Вес продукта (в килограммах или других единицах)
        self.category = category  # Категория продукта

    def __str__(self):
        # Возвращает строковое представление продукта в формате: 'Название, Вес, Категория'
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        # Инкапсулированное имя файла, в котором хранятся данные о продуктах
        self.__file_name = 'products.txt'

    def get_products(self):
        # Метод для чтения всех продуктов из файла
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()  # Считываем содержимое файла и удаляем лишние пробелы
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустую строку
            return ""

    def add(self, *products):
        # Метод для добавления одного или нескольких продуктов в файл

        # Считываем существующие продукты из файла и сохраняем их в виде множества
        existing_products = set(
            line.strip() for line in self.get_products().splitlines()
        )

        # Открываем файл в режиме добавления
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:  # Перебираем переданные продукты
                product_str = str(product)  # Преобразуем объект Product в строку
                if product_str in existing_products:
                    # Если продукт уже есть в списке, выводим сообщение
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    # Если продукта нет, добавляем его в файл и множество
                    file.write(product_str + '\n')
                    existing_products.add(product_str)

# Пример использования:
s1 = Shop()

# Создаём несколько объектов Product
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Выводим строковое представление одного из продуктов
print(p2)  # __str__

# Добавляем продукты в магазин (в файл)
s1.add(p1, p2, p3)

# Выводим список продуктов из файла
print(s1.get_products())
