from controller.user_controller import UserController

def template():
    address_state = input('Insira o estado do usuário, deixe o campo em branco para listar todos: ')
    print(UserController.get_users(address_state))