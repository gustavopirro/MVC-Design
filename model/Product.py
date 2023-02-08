from db.mock_db import Database
from model import Product


class Product:

    def __init__(self, product_name: str = None, product_flavor: str = None) -> None:
        self.product_name = product_name
        self.product_flavor = product_flavor

    def insert(self): # O que colocar na tip de retorno deste metodo? visto que é possível retornar um erro ou uma string

        # Queria fazer essa validação de forma generica para todos os campos e classes model, mas não soube fazer.
        # Algo como:
        # for field in instance.fields.required:
        #   validate_field(field)
        if not self.product_name or not self.product_flavor:
            raise 'Products field must not be None.'
        
        new_product = {'product_name': self.product_name, 'product_flavor': self.product_flavor}
        Database().product_table.append(new_product)

        return new_product

    def get_all(self) -> object:
        return Database().product_table

    def delete(self, product_name):
        element_index = self.__find_element_index(product_name)
        
        if(element_index == -1):
            return 'Product not found.'

        Database.product_table.pop(element_index)
        return 'Product deleted.'


    def __find_element_index(self, element_name:str) -> int:
        for i, product in enumerate(Database().product_table):
            if product.get('product_name') == element_name:
                return i
        return -1