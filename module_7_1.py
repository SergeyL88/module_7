import os.path


class Product:

    def __init__(self, name: str, weight: int | float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __repr__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as result:
                return result.read()
        except FileNotFoundError:
            print('Ничего нет')

    def add(self, *products):
        for product in products:
            if not os.path.exists(self.__file_name):
                temp_file = open(self.__file_name, 'w')
                temp_file.write(f'{product}\n')
                temp_file.close()
            elif str(product) in self.get_products():
                print(f'Продкут {product} уже есть в магазине')
            elif os.path.exists(self.__file_name):
                temp_file = open(self.__file_name, 'a')
                temp_file.write(f'{product}\n')
                temp_file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spagetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
