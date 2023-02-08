from controller.product_controller import ProductController


def template():
    print(ProductController().get_all())