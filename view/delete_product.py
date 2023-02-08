from controller.product_controller import ProductController

def template():
    product_name = input('Insira o nome do produto: ')
    print(ProductController().delete(product_name))