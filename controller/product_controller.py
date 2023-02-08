from model.Product import Product


class ProductController:

    def register(self, product_name: str, product_flavor: str) -> object:
        return Product(product_name, product_flavor).insert()

    def get_all(self):
        return Product().get_all()

    def delete(self, product_name):
        return Product().delete(product_name)