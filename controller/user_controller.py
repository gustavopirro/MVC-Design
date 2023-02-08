from model.User import User


class UserController:

    def register(self, username, telephone, user_city_state) -> object:
        return User(username, telephone, user_city_state).insert()

    def get_users(self, user_city_state=None) -> list: # O que colocar na tip de retorno aqui? uma função retorna list e outra dict
        
        # É um bom design utilizar o filtro dessa forma?
        #  ou seria melhor criar uma função separada?
        if user_city_state:
            return User().filter_by_state(user_city_state)

        return User().get_all()