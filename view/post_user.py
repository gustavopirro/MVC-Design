from controller.user_controller import UserController

def template():
    username = input('Insira o nome de usuário: ')
    telephone = input('Insira o telefone: ')
    address_state = input('Insira o estado: ')

    print(UserController().register(username, telephone, address_state))
    print('Usuário registrado!')




