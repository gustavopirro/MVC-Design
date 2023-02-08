from controller.product_controller import ProductController

def template():
    
    product_name = input('Insira o nome do produto: ')
    product_flavor = input('Insira o sabor do produto: ')

    print(ProductController().register(product_name, product_flavor))
    print('Produto cadastrado!')