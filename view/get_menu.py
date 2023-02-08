from view import delete_product, get_users, post_user, get_products, post_products

def get_menu():
    print('Menu Padaria:')
    print('1- Cadastrar Usuário.')
    print('2- Filtrar usuários.')
    print('3- Listar produtos.')
    print('4- Cadastrar produto.')
    print('5- Deletar produto.')
    print('6- Sair')

    user_choice = int(input('Escolha a opção desejada: '))

    if(user_choice == 1): post_user.template()
    elif(user_choice == 2): get_users.template()
    elif(user_choice == 3): get_products.template()
    elif(user_choice == 4): post_products.template()
    elif(user_choice == 5): delete_product.template()
    elif(user_choice == 6): exit()
    
    print('\n\n')
    get_menu()